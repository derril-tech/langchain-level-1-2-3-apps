import os
from dotenv import load_dotenv
from google.cloud import storage

# Load local environment variables
load_dotenv()

class Settings:
    def __init__(self):
        self.DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        self.DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
        self.APP_NAME = os.getenv("APP_NAME", "Full Stack PDF CRUD App")
        self.GCP_CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "secrets/gcs-key.json")
        self.GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")

    @staticmethod
    def get_gcs_client():
        import os
        from google.cloud import storage

        # Load path from env var (Render sets this)
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "secrets/gcs-key.json")
        print("📁 Using GCS creds path:", credentials_path)

        return storage.Client.from_service_account_json(credentials_path)


