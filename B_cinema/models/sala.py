from .base import ModeloBase, db

class Sala(ModeloBase):
    __tablename__ = 'salas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    capacidade = db.Column(db.Integer)

    @classmethod
    def listar(cls):
        return cls.query.all()
