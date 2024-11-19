import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:231281@localhost:3306/biometria'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:TBNOywoFaDKYPffcvvzcAmFWTiOQOaHv@postgres.railway.internal:5432/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit