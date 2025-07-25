
## main.py active et donne le travail à effectuer aux pipelines

from pipelines.pipeline_scraping import run_scraping_pipeline
from pipelines.pipeline_api import run_api_pipeline


def main():
    """Fonction principale pour exécuter les pipelines."""
    
    # Exécution du pipeline de scraping avec les valeurs par défaut
    # 50 pages comme dans le notebook
    print("=== Exécution pipeline de scraping ===")
    run_scraping_pipeline(pages=50, save_raw_data=True)
    
    # Exécution du pipeline API
    print("\n=== Exécution pipeline API ===")
    run_api_pipeline()


# Le fichier ne sera exécuté seulement si on appelle ce dernier avec python3 main.py
if __name__ == "__main__":
    main()