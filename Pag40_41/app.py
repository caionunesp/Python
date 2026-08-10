from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import requests

app = Flask(__name__)
app.secret_key = 'sua_secret_key_super_segurna'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
            conn.commit()
        except sqlite3.IntegrityError:
            return "E-mail já cadastrado!"
        finally:
            conn.close()
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        conn = get_db_connection()
        usuario = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        conn.close()
        if usuario and check_password_hash(usuario['senha'], senha):
            session['user_id'] = usuario['id']
            session['user_name'] = usuario['nome']
            return redirect(url_for('dashboard'))
        return "Credenciais inválidas!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    
    status_filter = request.args.get('status')
    conn = get_db_connection()
    if status_filter in ['Pendente', 'Em andamento', 'Concluída']:
        tarefas = conn.execute('SELECT * FROM tarefas WHERE usuario_id = ? AND status = ?', (session['user_id'], status_filter)).fetchall()
    else:
        tarefas = conn.execute('SELECT * FROM tarefas WHERE usuario_id = ?', (session['user_id'],)).fetchall()
    conn.close()

    frase_motivacional = "Acredite no seu potencial!"
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=2)
        if response.status_code == 200:
            frase_motivacional = response.json().get('slip', {}).get('advice', frase_motivacional)
    except: pass
    return render_template('dashboard.html', tarefas=tarefas, frase=frase_motivacional)

@app.route('/dados_progresso')
def dados_progresso():
    if 'user_id' not in session: return jsonify({})
    conn = get_db_connection()
    data = conn.execute('SELECT status, COUNT(*) as count FROM tarefas WHERE usuario_id = ? GROUP BY status', (session['user_id'],)).fetchall()
    conn.close()
    
    resultado = {item['status']: item['count'] for item in data}
    return jsonify(resultado)

@app.route('/dashboard_progresso')
def dashboard_progresso():
    if 'user_id' not in session: return redirect(url_for('login'))
    return render_template('progresso.html')

@app.route('/nova_tarefa', methods=['GET', 'POST'])
def nova_tarefa():
    if 'user_id' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)',
                     (request.form['titulo'], request.form['descricao'], request.form['status'], session['user_id']))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('nova_tarefa.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    if request.method == 'POST':
        conn.execute('UPDATE tarefas SET titulo=?, descricao=?, status=? WHERE id=? AND usuario_id=?',
                     (request.form['titulo'], request.form['descricao'], request.form['status'], id, session['user_id']))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    tarefa = conn.execute('SELECT * FROM tarefas WHERE id=? AND usuario_id=?', (id, session['user_id'])).fetchone()
    conn.close()
    return render_template('editar_tarefa.html', tarefa=tarefa)

@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id=? AND usuario_id=?', (id, session['user_id']))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)