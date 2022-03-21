import os

basedir = os.path.abspath(os.path.dirname(__file__))

#DBの名前・ファイルの場所　設定
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'web/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #flask-wtfを利用するために必須
    SECRET_KEY = 'my-secret_key'
    ITEMS_PER_PAGE = 5