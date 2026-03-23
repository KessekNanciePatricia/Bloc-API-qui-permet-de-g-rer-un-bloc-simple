# Bloc-API-qui-permet-de-g-rer-un-bloc-simple
Développer un bloc API 
description des endpoints


Création d’un article (POST /api/articles)
    • Méthode : POST
    • URL : /api/articles
    • Body (JSON) :
{"titre": "programmation",
     "contenu": "programation web en flask", 
     "auteur": "rayane", 
     "date_poste": "2026-03-18", 
     "categorie": "tech", 
     "tags": "pour dev"
}

    • Résultat obtenu :
        ◦ Code HTTP : 201 (Création réussie)
        ◦ Réponse :
{
  "message": "Ajout reussi",
  "id": 1
}
 Ce test confirme que l’insertion dans la base de données fonctionne correctement.
 b) Récupération de tous les articles (GET /api/articles)
    • Méthode : GET
    • URL : /api/articles
    • Résultat obtenu :
        ◦ Code HTTP : 200 (OK)
        ◦ Réponse : tableau JSON contenant les articles
Ce test permet de vérifier la lecture globale des données.
 c) Récupération d’un article spécifique (GET /api/articles/{id})
    • Méthode : GET
    • URL : /api/articles/1
    • Résultat obtenu :
        ◦ Code HTTP : 200 (OK)
        ◦ Réponse : informations complètes de l’article
Si l’article n’existe pas :
    • Code HTTP : 404 (Not Found)
 d) Modification d’un article (PUT /api/articles/{id})
    • Méthode : PUT
    • URL : /api/articles/1
    • Body (JSON) :
{
  "titre": "Article modifié",
  "contenu": "Nouveau contenu"
}
    • Résultat obtenu :
        ◦ Code HTTP : 200 (OK)
        ◦ Réponse : confirmation de modification
Ce test valide la mise à jour des données dans la base.
 e) Suppression d’un article (DELETE /api/articles/{id})
    • Méthode : DELETE
    • URL : /api/articles/1
    • Résultat obtenu :
        ◦ Code HTTP : 200 (OK)
        ◦ Réponse : message de confirmation
Vérification supplémentaire :
    • l’article n’apparaît plus dans la liste

    
