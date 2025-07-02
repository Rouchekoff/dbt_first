import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from dbt-init!")

    # Paramètres de connexion depuis les variables d'environnement
    username = os.getenv("DB_USERNAME", "root")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    database = os.getenv("DB_NAME", "my_dbt_db")

    if not password:
        print("Erreur: Veuillez définir la variable d'environnement DB_PASSWORD")
        return

    # Création de la connexion
    DATABASE_URI = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(DATABASE_URI)

    # Création de la base de données si elle n'existe pas
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Base de données '{database}' créée.")

    # Chargement des données CSV
    liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]
    for table in liste_tables:
        csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
        df = pd.read_csv(csv_url)
        df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
        print(f"Table 'raw_{table}' chargée avec {len(df)} lignes.")


if __name__ == "__main__":
    main()
