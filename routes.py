from flask import Blueprint, jsonify, request, session
from .models import Article
from sqlalchemy import or_
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "hello"

@main.route('/api/articles', methods=["GET"])
def get_article():
    try:
        articles = Article.query.all()
        
        if not articles:
            return jsonify({'message': 'aucun article trouvé'}),  404
        output = []
        for a in articles:
            
            data = {
                'id': a.id,
                'titre': a.titre,
                'contenu': a.contenu,
                'auteur': a.auteur,
                'date': a.date_poste,
                'categorie': a.categorie,
                'tags': a.tags
            }
            output.append(data)
        return jsonify({'articles': output})
    except Exception as e:
        return f"Erreur: {e}"

@main.route('/api/articles', methods=["POST"])
def ajouter():
    data = request.get_json()

    titre = data.get('titre')
    contenu = data.get('contenu')
    auteur = data.get('auteur')
    date_poste = data.get('date_poste')
    categorie = data.get('categorie')
    tags = data.get('tags')

    article = Article(
        titre=titre,
        contenu=contenu,
        auteur=auteur,
        date_poste=date_poste,
        categorie=categorie,
        tags=tags
    )

    db.session.add(article)
    db.session.commit()

    return jsonify({"message": "ajout reuissi", "id": article.id})

@main.route('/api/articles/<int:article_id>', methods=["GET"])
def recuperer_un_article(article_id):
    article = Article.query.get(article_id)

    if article is None:
        return jsonify({"message": "article introuvable"}), 404

    data = {
        "titre": article.titre,
        "contenu": article.contenu,
        "auteur": article.auteur,
        "date": article.date_poste,
        "categorie": article.categorie,
        "tags": article.tags
    }

    return jsonify(data)

@main.route('/api/articles/<int:article_id>', methods=["PUT"])
def modifier_article(article_id):
    article = Article.query.get(article_id)

    if article is None:
        return jsonify({"message": "article introuvable"}), 404
    
    data = request.get_json()

    article.titre = data.get('titre', article.titre)
    article.contenu = data.get('contenu', article.contenu)
    article.categorie = data.get('categorie', article.categorie)
    article.tags = data.get('tags', article.tags)

    db.session.commit()

    return jsonify({"message": "article mis a jour!!!"})

@main.route('/api/articles/<int:article_id>', methods=["DELETE"])
def supprimer(article_id):
    article = Article.query.get(article_id)

    if article is None:
        return jsonify({"message": "article introuvable"}), 404

    db.session.delete(article)
    db.session.commit()

    return jsonify({"message": f"l'article {article_id} a été supprimé avec succès"}),200

@main.route('/api/articles/search', methods=['GET'])
def search():
    query_param = request.args.get('q', '')
    if not query_param:
        return jsonify({'erreur': "veuillez fournir un mot clé"}), 400

    data = Article.query.filter(or_(Article.titre.ilike(f'%{query_param}%'), Article.contenu.ilike(f'%{query_param}%'))).all()

    if not data:
        return jsonify({'message': 'aucun article trouvé'}), 404

    result = []
    for a in data:
        result.append({
            "titre": a.titre, 
            "contenu": a.contenu, 
            "auteur": a.auteur, 
            "date": a.date_poste, 
            "categorie": a.categorie, 
            "tags": a.tags
        })

    return jsonify({"resultats": result})

