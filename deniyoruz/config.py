# class Config:
#     DB_HOST = 'localhost'
#     DB_USER = 'root'
#     DB_PASSWORD = ''
#     DB_NAME = 'chatbot'

from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Ortam değişkenlerini al
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))  # Port genellikle int olmalı
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
