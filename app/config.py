import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://APieceOfChalk:28515128@localhost/test1'
    SECRET_KEY = '123456'

    ### FLASK-SECURITY ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECORITY_PASSWORD_HASH = 'bcrypt'

    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = True


    # Flask-Mail settings
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'forsite2851@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'M123456l')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
    MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', True))
    SECURITY_EMAIL_SENDER = os.getenv('SECURITY_EMAIL_SENDER', 'forsite2851@gmail.com')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'forsite2851@gmail.com')

    # Flask-User settings
    USER_APP_NAME = "AppName"  # Used by email templates
