import os
from dotenv import load_dotenv


def get_connection_string():
    load_dotenv()
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    return f"postgresql://{user}:{password}@{host}:{port}/{database}"
