class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False