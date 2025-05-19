import os

from dotenv import load_dotenv

load_dotenv()

class ConfigDev:
    DEBUG = True

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False