# Book Data Collection Project

## Description

Ce projet permet de collecter des données de livres depuis **deux sources différentes** :

- **Scraping web** : Extraction de données depuis le site [books.toscrape.com](http://books.toscrape.com/)
- **API Google Books** : Récupération de données via l'API officielle Google Books

Les données sont ensuite traitées, nettoyées et stockées dans une base de données SQLite unifiée.

## Fonctionnalités

- **Scraping de 1000 livres** depuis books.toscrape.com  
- **Récupération via API Google Books** (livres filtrés avec prix et note)  
- **Traitement et nettoyage** des données  
- **Sauvegarde des données brutes** en CSV  
- **Base de données SQLite** centralisée  
- **Pipelines modulaires** et réutilisables  

## Structure du projet

```
book_scraping_project/
├── data/                           # Fichiers CSV de données brutes
│   ├── df_books.csv               # Données du scraping (1000 livres)
│   └── data_api.csv               # Données brutes de l'API (40 livres)
├── get_data/                      # Modules de récupération de données
│   ├── __init__.py
│   ├── get_scraping_data.py       # Scraping web
│   └── get_api_data.py            # API Google Books
├── process_data/                  # Modules de traitement des données
│   ├── __init__.py
│   ├── process_scrapping_data.py  # Traitement données scraping
│   └── process_api_data.py        # Traitement données API
├── database/                      # Module de gestion de base de données
│   ├── __init__.py
│   ├── insert_data.py            # Fonctions d'insertion en base
│   └── book_store.db             # Base de données SQLite
├── pipelines/                     # Pipelines de traitement complets
│   ├── __init__.py
│   ├── pipeline_scraping.py      # Pipeline scraping web
│   └── pipeline_api.py           # Pipeline API Google Books
├── main.py                       # Point d'entrée principal
├── requirements.txt              # Dépendances du projet
└── README.md                     # Ce fichier
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac ou .venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

## Utilisation

### Exécution complète
```bash
python3 main.py
```
Exécute les deux pipelines séquentiellement :
- **Scraping** : 1000 livres depuis books.toscrape.com
- **API** : ~10 livres filtrés depuis Google Books API

### Exécution séparée
```python
# Scraping uniquement
from pipelines.pipeline_scraping import run_scraping_pipeline
run_scraping_pipeline(pages=50, save_raw_data=True)

# API uniquement  
from pipelines.pipeline_api import run_api_pipeline
run_api_pipeline()
```

## Processus de traitement

**Pipeline scraping :** Scrape 50 pages → Sauvegarde CSV → Traitement → Création base de données  
**Pipeline API :** Requête Google Books → Filtrage (prix + note) → Ajout en base existante

## Base de données

**Fichier :** `database/book_store.db`  
**Table :** `book_store` avec colonnes `title`, `price`, `rating`, `availability`  
**Contenu final :** ~1010 livres (1000 scraping + 10 API)

## Données sauvegardées

- `data/df_books.csv` : Données brutes du scraping (1000 livres)
- `data/data_api.csv` : Données brutes de l'API (40 livres avant filtrage)
- `database/book_store.db` : Base finale (1010 livres)

