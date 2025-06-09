import os
from google.cloud import storage
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int = 5432
    APP_NAME: str = "Full Stack PDF CRUD App"
    GOOGLE_APPLICATION_CREDENTIALS: str = "secrets/gcs-key.json"
    GCP_BUCKET_NAME: str

    @staticmethod
    def get_gcs_client():
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "secrets/gcs-key.json")
        print("📁 Using GCS creds path:", credentials_path)
        return storage.Client.from_service_account_json(credentials_path)

    class Config:
        env_file = ".env"
        extra = "ignore"
