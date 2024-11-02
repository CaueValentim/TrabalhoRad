from flask import Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import Flask, request, jsonify 



app = Flask(__name__)
Api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #URI do banco de dados
db = SQLAlchemy(app)

from app.models.missoes import Missoes
with app.app_context():
  db.create_all()

from app.view.resoMissoes import Index,relatarMissao,mudançaDePlanos,abortarMissao,MissaoById
Api.add_resource(Index, "/")
Api.add_resource(relatarMissao, "/create")
Api.add_resource(mudançaDePlanos, "/update")
Api.add_resource(abortarMissao, "/delete")
Api.add_resource(MissaoById, "/search")

'''@app.route("/index")
def index():
  return render_template("index.html")'''
