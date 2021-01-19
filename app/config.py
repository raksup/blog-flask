import os

class Config:
    SECRET_KEY = '61cccbe9a0a9937e4c6103837fd70b8e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    #setup for sending emails
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')