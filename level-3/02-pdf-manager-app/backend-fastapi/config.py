import os
from dotenv import load_dotenv
from google.cloud import storage

# Load local environment variables
load_dotenv()

class Settings:
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
    APP_NAME = os.getenv("APP_NAME", "Full Stack PDF CRUD App")
    GCP_CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "secrets/gcs-key.json")
    GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")

    @staticmethod
    def get_gcs_client():
        return storage.Client.from_service_account_json(Settings.GCP_CREDENTIALS_PATH)
