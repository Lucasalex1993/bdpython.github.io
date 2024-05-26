# config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgre:1234@localhost:5432/meubanco')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
