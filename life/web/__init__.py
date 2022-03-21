from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

#Flaskのインスタンスを作成する
app = Flask(__name__)

#sqliteを参照する設定
app.config.from_object(Config)

#ランダムの文字列を秘密鍵に設定してくれる
#app.config['SECRET_KEY'] = os.urandom(24)

#テーブルとクラスを１対１に対応させるORM"SQLAlchemy"
db = SQLAlchemy(app)

#dbの内容変更などのメモを保存できる"Migrate"
migrate = Migrate(app, db)

#参照するために必須
from web import views, models