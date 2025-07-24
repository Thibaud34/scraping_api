import pandas as pd

# Créer une fonction convert_types qui combine les traitements faits dans les cellules précédentes
def convert_types(df_books: pd.DataFrame) -> pd.DataFrame:
    """Convert the types of the DataFrame columns to appropriate types.

    - 'title' en chaîne de caractères (str)
    - 'price' en float, sans le symbole '£'
    - 'availability' en booléen (True si 'In stock', False sinon)
    - 'rating' en entier (1 à 5)

    Args:
        df_books (pd.DataFrame): The DataFrame containing book data.

    Returns:
        pd.DataFrame: The DataFrame with converted types.
    """

    # Conversion de 'title' en chaîne de caractères
    df_books["title"] = df_books["title"].astype(str)

    # Nettoyage et conversion de 'price' en float (suppression du symbole £)
    df_books["price"] = df_books["price"].str.replace("£", "").astype(float)

    # Fonction interne pour convertir availability en booléen
    def convert_availability(value):
        if value == "In stock":
            return True
        return False

    df_books["availability"] = df_books["availability"].apply(convert_availability)

    # Dictionnaire de conversion pour rating
    ratings_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    # Application de la conversion sur la colonne rating
    df_books["rating"] = df_books["rating"].map(ratings_map)

    return df_books