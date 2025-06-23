from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
import models, schemas
from config import Settings
from google.cloud import storage
from google.api_core.exceptions import GoogleAPIError


def create_pdf(db: Session, pdf: schemas.PDFRequest):
    db_pdf = models.PDF(name=pdf.name, selected=pdf.selected, file=pdf.file)
    db.add(db_pdf)
    db.commit()
    db.refresh(db_pdf)
    return schemas.PDFResponse.from_orm(db_pdf)


def read_pdfs(db: Session, selected: bool = None):
    if selected is None:
        pdfs = db.query(models.PDF).all()
    else:
        pdfs = db.query(models.PDF).filter(models.PDF.selected == selected).all()
    return [schemas.PDFResponse.from_orm(pdf) for pdf in pdfs]


def read_pdf(db: Session, id: int):
    pdf = db.query(models.PDF).filter(models.PDF.id == id).first()
    if pdf:
        return schemas.PDFResponse.from_orm(pdf)
    return None


def update_pdf(db: Session, id: int, pdf: schemas.PDFRequest):
    db_pdf = db.query(models.PDF).filter(models.PDF.id == id).first()
    if db_pdf is None:
        return None
    update_data = pdf.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pdf, key, value)
    db.commit()
    db.refresh(db_pdf)
    return schemas.PDFResponse.from_orm(db_pdf)


def delete_pdf(db: Session, id: int):
    db_pdf = db.query(models.PDF).filter(models.PDF.id == id).first()
    if db_pdf is None:
        return None
    db.delete(db_pdf)
    db.commit()
    return True


def upload_pdf(db: Session, file: UploadFile, file_name: str):
    client = Settings.get_gcs_client()
    bucket = client.bucket(Settings().GCP_BUCKET_NAME)
    blob = bucket.blob(file_name)

    try:
        # Upload the file to GCS
        blob.upload_from_file(file.file, content_type=file.content_type)

        # ✅ Make the file publicly accessible
        blob.make_public()

        # Build the public URL
        file_url = f"https://storage.googleapis.com/{bucket.name}/{file_name}"

        # Save metadata in DB
        db_pdf = models.PDF(name=file.filename, selected=False, file=file_url)
        db.add(db_pdf)
        db.commit()
        db.refresh(db_pdf)

        return schemas.PDFResponse.from_orm(db_pdf)

    except GoogleAPIError as e:
        raise HTTPException(status_code=500, detail=f"GCS error: {str(e)}")

    # --- Original version without public access ---
    # blob.upload_from_file(file.file, content_type=file.content_type)
    # file_url = f"https://storage.googleapis.com/{bucket.name}/{file_name}"
    # (No .make_public() here)
    #----------------------------
    # Why This Works:
#blob.make_public() makes the uploaded file accessible via public link — exactly what PyPDFLoader() requires.

#You preserve all the original logic in comments — just delete the line with .make_public() to revert back if needed.

