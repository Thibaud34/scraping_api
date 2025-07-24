import pandas as pd

def filter_and_prepare_api_data(df_books):
    """
    Filtre et prépare les données de l'API avant insertion en base
    """
    print("Filtrage et préparation des données...")
    
    # Filtrer les livres pour ne conserver que ceux ayant des valeurs pour les colonnes price et rating
    df_books_filtered = df_books.dropna(subset=['price', 'rating'])
    print(f"Après filtrage : {len(df_books_filtered)} livres conservés")
    
    # Réinitialiser les index du DataFrame  
    df_books_filtered = df_books_filtered.reset_index(drop=True)
    
    # Ajouter une colonne availability = False
    df_books_filtered['availability'] = False
    
    print("Préparation des données terminée")
    return df_books_filtered

def save_raw_data_to_csv(df_books):
    """
    Sauvegarde les données brutes dans un fichier CSV
    """
    print("Sauvegarde des données brutes...")
    
    # Sauvegarder les données brutes dans data/data_api.csv
    df_books.to_csv('data/data_api.csv', index=False)
    
    print("Données sauvegardées dans data/data_api.csv")