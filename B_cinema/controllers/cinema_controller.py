# Cenário: B - Cinema
# Aluno: Seu Nome

from flask import Blueprint, redirect, render_template, request, url_for
from datetime import datetime
from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    # 1. CORREÇÃO: Busca as sessões reais do banco
    sessoes = Sessao.listar_com_detalhes()
    # Passa a variável 'sessoes' real para o HTML renderizar a tabela
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        data_hora = request.form.get("data_hora")
        preco = request.form.get("preco")
        
        data_hora_objeto = datetime.strptime(data_hora, "%Y-%m-%dT%H:%M")
        
        nova_sessao = Sessao(
            filme_id=int(filme_id),
            sala_id=int(sala_id),
            data_hora=data_hora_objeto,
            preco=float(preco)
        )
        db.session.add(nova_sessao)
        db.session.commit()

        # 2. CORREÇÃO: Redireciona para a lista após salvar com sucesso
        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
