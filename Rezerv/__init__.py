from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import base64

def hide_this(st_input):
     return base64.b64decode(st_input).decode("utf-8")

app = Flask(__name__)
#on Server
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sjanotak_2366:'+hide_this('SXpwaXBlMis=')+'@store5.rosti.cz:3306/sjanotak_2366'
#shh
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sjanotak_2366:'+hide_this('SXpwaXBlMis=')+'@localhost:3306/sjanotak_2366'
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



