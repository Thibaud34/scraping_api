import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fonction pour extraire le titre d'un livre
def extract_title(book: BeautifulSoup) -> str:
    """ Extract the title of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book (typically a <article class="product_pod">).

    Returns:
        str: The title of the book.
    """
# Pour le premier livre
    title = book.h3.a['title']
    return title


# Fonction pour extraire le prix d'un livre
def extract_price(book: BeautifulSoup) -> str:
    """Extract the price of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The price of the book.
    """
    price = book.find('p', class_='price_color').text
    return price


# Fonction pour extraire la note d'un livre
def extract_rating(book: BeautifulSoup) -> str:
    """Extract the rating of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The rating of the book.
    """
    rating = book.find('p', class_='star-rating').get("class")[1]
    return rating


# Fonction pour extraire la disponibilité d'un livre
def extract_availability(book: BeautifulSoup) -> str:
    """Extract the availability of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The availability of the book.
    """
    availability = book.find('p', class_='instock availability').text.strip()
    return availability


# Fonction qui combine les informations d'un livre dans un dictionnaire
def extract_book_info(book: BeautifulSoup) -> dict:
    """
    Extrait les informations d'un livre à partir d'un élément HTML <article class="product_pod">.

    Args:
        book (BeautifulSoup): L'élément HTML du livre.

    Returns:
        dict: Un dictionnaire contenant le titre, le prix, la note et la disponibilité.
    """
    
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.find('p', class_='star-rating').get("class")[1]
    availability = book.find('p', class_='instock availability').text.strip()

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
    }


def get_books_html(url: str) -> BeautifulSoup:
    """Fetch the HTML content of a book page.

    Args:
        url (str): The URL of the book page.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the HTML content.
    """
    response = requests.get(url)

# On stocke le contenu HTML dans une variable
    html_content = response.content

# On crée un objet BeautifulSoup pour parser le HTML
    soup = BeautifulSoup(html_content, "html.parser")

    return soup


# Parcourir les pages et récupérer les livres
def scrape_books(pages: int) -> list[dict]:
    """Scrape books from the specified number of pages.

    Args:
        pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries containing books information.
    """
    # Créer une variable base_url
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    
    # Créer une liste qui contiendra tous les dictionnaires scrapés
    all_books = []
    
    # Pour chaque page
    for page_num in range(1, pages + 1):
        # Construire l'URL adapté
        url = base_url.format(page_num)
        
        # Utiliser la fonction get_books_html pour récupérer les livres de la page
        soup = get_books_html(url)
        
        # Trouver tous les livres sur la page
        books = soup.find_all('article', class_='product_pod')
        
        # Utiliser la compréhension de liste et la fonction extract_book_info
        data_books = [extract_book_info(book) for book in books]
        
        # Ajouter les livres de cette page à la liste globale
        all_books.extend(data_books)
    
    return all_books