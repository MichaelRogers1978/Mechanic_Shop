import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        "title": "Mechanic Shop",
        "uiversion": 3
    }

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = False
    CACHE_TYPE = 'SimpleCache'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234ThumbWar@localhost/Mechanic_Shop'
    DEBUG = True

class TestingConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgresql://mikerogers:6ES8Ys6IGMUQODfS80nWkzcjlKhcbcjj@dpg-d2n7vkvdiees73ca3ing-a.oregon-postgres.render.com/mechanic_shop_project")
    WTF_CSRF_ENABLED = False
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}