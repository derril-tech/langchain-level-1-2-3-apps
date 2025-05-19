import os
from pydantic_settings import BaseSettings
from google.cloud import storage

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack PDF CRUD App"
    GOOGLE_APPLICATION_CREDENTIALS: str
    GCP_BUCKET_NAME: str

    @staticmethod
    def get_gcs_client():
        return storage.Client.from_service_account_json(Settings().GOOGLE_APPLICATION_CREDENTIALS)

    class Config:
        env_file = ".env"
        extra = "ignore"
