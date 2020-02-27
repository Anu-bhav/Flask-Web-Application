

class Config:
    SECRET_KEY = '8aa2e62480a55d23b269ba558d10bb4d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # the 3 /// are a relative path from the current file
    MAIL_SERVER = 'mail.local'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'app@mail.local'
    MAIL_PASSWORD = 'Password'
