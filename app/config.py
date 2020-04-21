class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://APieceOfChalk:28515128@localhost/test1'
    SECRET_KEY = '123456'

    ### FLASK-SECURITY ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECORITY_PASSWORD_HASH = 'bcrypt'