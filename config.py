class Config:
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://rayane:Raymore@localhost/blog"