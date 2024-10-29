from app import db

#Criação da tabela
class Missoes(db.Model):
  __tablename__ = 'missões'
  __table_args__ = {'sqlite_autoincrement': True}
  id = db.Column(db.Integer, primary_key=True)
  nomeMissao = db.Column(db.String(255))
  dataLançamento = db.Column(db.Date)
  destino = db.Column(db.String)
  estadoMissao = db.Column(db.String)
  tripulacao = db.Column(db.String)
  cargaUtil = db.Column(db.String)
  duracaoMissao = db.Column(db.String)
  custoMissao = db.Column(db.Float)
  statusMissao = db.Column(db.String)

#Funções
  def __init__(self, nomeMissao,dataLançamento,destino,estadoMissao,tripulacao,cargaUtil, duracaoMissao, custoMissao, statusMissao):
    self.nomeMissao = nomeMissao
    self.dataLançamento = dataLançamento
    self.destino = destino
    self.estadoMissao = estadoMissao
    self.tripulacao = tripulacao
    self.cargaUtil = cargaUtil
    self.duracaoMissao = duracaoMissao
    self.custoMissao = custoMissao
    self.statusMissao = statusMissao

  
  def relatarMissao(self,nomeMissao,data_lançamento,destino,estadoMissao,tripulacao,cargaUtil,duracaoMissao,custoMissao,statusMissao):
    try:
      add_banco = Missoes(nomeMissao,data_lançamento,destino,estadoMissao,tripulacao,cargaUtil,duracaoMissao,custoMissao,statusMissao)
      db.session.add(add_banco)
      db.session.commit()
    except Exception as e:
      print(e)

  def mudançaDePlanos(self, id, nomeMissao,destino,estadoMissao,tripulacao,cargaUtil,duracaoMissao, custoMissao,statusMissao):
    try:
      db.session.query(Missoes).filter
      (Missoes.id == id).update({"id": id,"nomeMissao": nomeMissao, "destino":destino, "estadoMissao": estadoMissao, "tripulacao": tripulacao, "cargaUtil": cargaUtil, "duracaoMissao": duracaoMissao, "custoMissao": custoMissao, "statusMissao": statusMissao})
      db.session.commit()
    except Exception as e:
      print(e)
  
@staticmethod
def abortarMissao(self,id):
    try:
      db.session.query(Missoes).filter(Missoes.id == id).delete()
      db.session.commit()
    except Exception as e:
        print(e)






