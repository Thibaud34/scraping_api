# Importer les bibliothèques nécessaires
import requests
import json
import pandas as pd

def get_books_from_google_api():
    """
    Récupère les livres depuis l'API Google Books
    Retourne la liste des livres
    """
    print("Récupération des données depuis l'API Google Books...")
    
    # URL de l'API Google Books
    url = "https://www.googleapis.com/books/v1/volumes"
    
    # Dictionnaire de paramètres pour la requête
    params = {
        "q": "food",
        "filter": "paid-ebooks",
        "maxResults": 40,
        "orderBy": "relevance"
    }
    
    # Requêter l'API Google Books
    response = requests.get(url, params=params)
    
    # Vérifier le code de statut de la réponse
    print(f"Code de statut de la réponse : {response.status_code}")
    
    if response.status_code == 200:
        # Récupérer le coeur de la réponse
        data_books_raw = response.json()
        
        # Récupérer les données relatives aux livres via la clé 'items'
        data_books = data_books_raw.get('items', [])
        
        print(f"Nombre de livres récupérés : {len(data_books)}")
        return data_books
    else:
        print("Erreur lors de la récupération des données")
        return []

def create_books_list(data_books):
    """
    Crée une liste de dictionnaires à partir des données de l'API
    """
    print("Création de la liste de dictionnaires...")
    
    # Création d'une liste de dictionnaires pour les livres
    books_list = []
    
    for book in data_books:
        book_dict = {
            "title": book.get('volumeInfo', {}).get('title'),
            "price": book.get('saleInfo', {}).get('listPrice', {}).get('amount'),
            "rating": book.get('volumeInfo', {}).get('averageRating')
        }
        books_list.append(book_dict)
    
    print(f"Liste créée avec {len(books_list)} livres")
    return books_list

def create_dataframe_from_api(books_list):
    """
    Crée un dataframe à partir de la liste de dictionnaires
    """
    print("Création du DataFrame...")
    
    # Créer un dataframe à partir de la liste de dictionnaires
    df_books = pd.DataFrame(books_list)
    
    print(f"DataFrame créé avec {df_books.shape[0]} lignes et {df_books.shape[1]} colonnes")
    return df_books