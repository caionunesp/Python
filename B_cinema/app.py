import os
import sys

diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
if diretorio_projeto not in sys.path:
    sys.path.insert(0, diretorio_projeto)

from flask import Flask
from models import db
from controllers.cinema_controller import cinema_bp
from controllers.dashboard_controller import dashboard_bp

def criar_app():
    # Descobre o caminho absoluto da pasta raiz do projeto atual
    pasta_raiz = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        # Vincula as pastas usando caminhos absolutos para o Flask nunca se perder
        template_folder=os.path.join(pasta_raiz, "views", "templates"),
        static_folder=os.path.join(pasta_raiz, "views", "static"),
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta_raiz, "cinema.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(cinema_bp)

    with app.app_context():
        db.create_all()
        popular_dados()

    return app

def popular_dados():
    """Insere filmes e salas de teste se o banco estiver vazio."""
    from models import Filme, Sala
    
    if Filme.query.count() == 0:
        filme1 = Filme(titulo="Matrix", duracao=136)
        filme2 = Filme(titulo="Avatar: O Caminho da Água", duracao=192)
        filme3 = Filme(titulo="O Rei Leão", duracao=118)
        db.session.add_all([filme1, filme2, filme3])
        
    if Sala.query.count() == 0:
        sala1 = Sala(nome="Sala 01 IMAX", capacidade=150)
        sala2 = Sala(nome="Sala 02 3D Prime", capacidade=80)
        sala3 = Sala(nome="Sala 03 Standard", capacidade=120)
        db.session.add_all([sala1, sala2, sala3])

    db.session.commit()


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
