from flask_restful import Resource,reqparse
from app.models.missoes import Missoes
from datetime import datetime



#adicionar
argumentos = reqparse.RequestParser()
argumentos.add_argument('id', type=int)
argumentos.add_argument('nomeMissao', type=str)
argumentos.add_argument('dataLançamento', type=str)
argumentos.add_argument('destino', type=str)
argumentos.add_argument('estadoMissao', type=str)
argumentos.add_argument('tripulacao', type=str)
argumentos.add_argument('cargaUtil', type=str)
argumentos.add_argument('duracaoMissao', type=str)
argumentos.add_argument('custoMissao', type=float)
argumentos.add_argument('statusMissao', type=str)

#atualizar
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('nomeMissao', type=str)
argumentos_update.add_argument('destino', type=str)
argumentos_update.add_argument('estadoMissao', type=str)
argumentos_update.add_argument('tripulacao', type=str)
argumentos_update.add_argument('cargaUtil', type=str)
argumentos_update.add_argument('duracaoMissao', type=str)
argumentos_update.add_argument('custoMissao', type=float)
argumentos_update.add_argument('statusMissao', type=str)

#deletar
argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)



from flask import jsonify
class Index(Resource):
  def get(self):
    return jsonify("Seja Bem vindo a estação espacial DEEP SPACE NINE")
  
class relatarMissao(Resource):
    def post(self):
      try:
        datas = argumentos.parse_args()
        data_lancamento_str = datas['dataLançamento']
        data_lancamento = datetime.strptime(data_lancamento_str, '%d-%m-%Y').date()
        Missoes.relatarMissao(self,datas['nomeMissao'],data_lancamento,datas['destino'],datas['estadoMissao'],datas['tripulacao'],datas['cargaUtil'],datas['duracaoMissao'],datas['custoMissao'],datas['statusMissao'])
        return{"menssagem": 'Missão Cadastrada com sucesso'}

      except Exception as e:
        return jsonify({'status':500, 'msg':f'{e}'})
      
class mudançaDePlanos(Resource):
  def put(self):
    try:
      datas = argumentos_update.parse_args()
      Missoes.mudançaDePlanos(self,datas['id'],datas['nomeMissao'],datas['destino'],datas['estadoMissao'],datas['tripulacao'],datas['cargaUtil'],datas['duracaoMissao'],datas['custoMissao'],datas['statusMissao']) 
      return{"menssagem": 'Missão atualizadacom sucesso'}

    except Exception as e:
      return jsonify({'status':500, 'msg':f'{e}'})
    
class abortarMissao(Resource):
    def delete(self):
      try:     
        datas = argumentos_delete.parse_args()
        Missoes.abortarMissao(self,datas['id'],) 
        return{"menssagem": 'Missão atualizadacom sucesso'}

      except Exception as e:
        return jsonify({'status':500, 'msg':f'{e}'})
