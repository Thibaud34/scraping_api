import sqlite3
import pandas as pd

def create_and_insert_data(df_books: pd.DataFrame, db_path: str = "book_store.db") -> int:
    connection = sqlite3.connect(db_path)
    df_books.to_sql('book_store', connection, if_exists='replace', index=False)
    print("Nombre de modifications :", connection.total_changes)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_store")
    nb_livres = cursor.fetchone()[0]
    print("Nombre de livres dans la base :", nb_livres)
    connection.close()
    return nb_livres

def insert_api_data_to_database(df_books_filtered: pd.DataFrame, db_path: str = "database/book_store.db") -> int:
    print("Insertion des données de l'API en base de données...")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM book_store")
    books_before = cursor.fetchone()[0]
    print(f"Nombre de livres avant ajout : {books_before}")
    df_books_filtered.to_sql('book_store', connection, if_exists='append', index=False)
    cursor.execute("SELECT COUNT(*) FROM book_store")
    books_after = cursor.fetchone()[0]
    print(f"Nombre de livres après ajout : {books_after}")
    connection.close()
    return books_after - books_before