import os
import sys
import pandas as pd

# Méthode simple : ajouter le parent au path et tout devrait fonctionner
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from get_data.get_scraping_data import scrape_books
from process_data.process_scraping_data import convert_types  
from database.insert_data import create_and_insert_data


def run_scraping_pipeline(pages: int = 50, save_raw_data: bool = True) -> None:
    """
    Execute le pipeline complet de scraping, traitement et stockage des données.
    
    Args:
        pages (int): Nombre de pages à scraper (par défaut 50).
        save_raw_data (bool): Si True, sauvegarde les données brutes en CSV.
    """
    print("Début du pipeline de scraping...")
    
    # Étape 1 : Scraping des données
    print("Scraping des données...")
    data_books = scrape_books(pages)
    print(f"{len(data_books)} livres scrapés")
    
    # Conversion en DataFrame
    df_books = pd.DataFrame(data_books)
    
    # Sauvegarde des données brutes
    if save_raw_data:
        # Création du dossier data s'il n'existe pas
        os.makedirs("data", exist_ok=True)
        
        # Sauvegarde dans un fichier CSV (UTF-8 pour les accents)
        df_books.to_csv("data/df_books.csv", index=False, encoding='utf-8')
        print("Fichier CSV 'df_books.csv' sauvegardé avec succès.")
    
    # Étape 2 : Traitement des données
    print("Traitement des données...")
    df_books = convert_types(df_books)
    
    # Étape 3 : Insertion en base de données
    print("Insertion en base de données...")
    nb_livres = create_and_insert_data(df_books)
    
    print(f"Pipeline terminé! {nb_livres} livres dans la base de données.")