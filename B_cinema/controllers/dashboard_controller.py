from flask import Blueprint, render_template
from models import Filme, Sala, Sessao

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/")

@dashboard_bp.route("/")
def index():
    total_filmes = len(Filme.listar())
    total_salas = len(Sala.listar())
    total_sessoes = len(Sessao.listar_com_detalhes())
    
    return render_template(
        "dashboard.html", 
        total_filmes=total_filmes, 
        total_salas=total_salas, 
        total_sessoes=total_sessoes
    )
