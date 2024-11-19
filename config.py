import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:231281@localhost:3306/biometria'
    SQLALCHEMY_DATABASE_URI = 'postgresql://professor:iDfH9ycUjexAPX6nhWYxGSvvtboq3y16@dpg-cstp5jjtq21c73bpbsig-a.oregon-postgres.render.com/faceid'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit