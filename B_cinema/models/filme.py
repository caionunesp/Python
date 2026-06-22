from .base import ModeloBase, db

class Filme(ModeloBase):
    __tablename__ = 'filmes'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracao = db.Column(db.Integer)

    @classmethod
    def listar(cls):
        return cls.query.all()
