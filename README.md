# Mon Projet DBT

## Installation

1. Clonez ce repository
2. Installez les dépendances : `pip install -r requirements.txt` avec:
   "dbt-core",
    "dbt-mysql",
    "pandas",
    "pymysql",
    "sqlalchemy",
    "sqlalchemy_utils",
    "cryptography",
   "python-dotenv"
4. Configurez vos variables d'environnement :
   ```bash
   export DB_USERNAME=your_username
   export DB_PASSWORD=your_password
   export DB_HOST=localhost
   export DB_PORT=3306
   export DB_NAME=my_dbt_db
