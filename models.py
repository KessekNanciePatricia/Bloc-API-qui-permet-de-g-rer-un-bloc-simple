from . import db
from sqlalchemy import Date

class Article(db.Model):
    __tablename__ = "Article"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    contenu = db.Column(db.String(100), nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    date_poste = db.Column(db.Date, nullable=False)
    categorie = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<article {self.titre}>"