import os

class Config:
    SECRET_KEY = 'cc36e909fbe851eca8de84699919c8b6e13d3b77'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USE_SSL = False