# Importer les fonctions des autres modules
from get_data.get_api_data import get_books_from_google_api, create_books_list, create_dataframe_from_api
from process_data.process_api_data import filter_and_prepare_api_data, save_raw_data_to_csv
from database.insert_data import insert_api_data_to_database

def run_api_pipeline():
    """
    Fonction qui effectue l'ensemble des traitements pour l'API
    """
    print("=== DÉBUT DU PIPELINE API ===")
    
    # Étape 1 : Scraper les données sous forme d'un dataframe
    print("\n1. Récupération des données depuis l'API...")
    data_books = get_books_from_google_api()
    
    if not data_books:
        print("Aucune donnée récupérée. Arrêt du pipeline.")
        return
    
    # Créer la liste de dictionnaires
    books_list = create_books_list(data_books)
    
    # Créer le DataFrame
    df_books = create_dataframe_from_api(books_list)
    
    # Étape 2 : Sauvegarder les données brutes
    print("\n2. Sauvegarde des données brutes...")
    save_raw_data_to_csv(df_books)
    
    # Étape 3 : Préparer les données avant de les mettre en base
    print("\n3. Préparation des données pour la base...")
    df_books_filtered = filter_and_prepare_api_data(df_books)
    
    # Étape 4 : Insérer les données en base (CORRIGÉ)
    print("\n4. Insertion des données en base...")
    nb_livres_ajoutes = insert_api_data_to_database(df_books_filtered, db_path="book_store.db")
    
    print(f"\n=== PIPELINE API TERMINÉ - {nb_livres_ajoutes} livres ajoutés ===")
    return df_books_filtered