import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:231281@localhost:3306/biometria'
    SQLALCHEMY_DATABASE_URI = 'postgres://ue56gacpg836tn:p67660c244347c8e12a5ac3dc56799125e2970fea3a952b4d464f79c0755dcd15@ccpa7stkruda3o.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d2980vnprjccv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit