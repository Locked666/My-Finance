from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey, Text, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import os 
from pathlib import Path


# Cria o caminho para o banco de dados no diretório pai
PATH = Path(__file__).parent 
path_db = os.path.join(PATH, 'database', 'database.db')

CONN = f"sqlite:///{path_db}"

engine = create_engine(CONN,echo=True)
Session =  sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cnpj_cpf = Column(String)
    data_abertura = Column(Date)

class Parametros(Base):
    __tablename__='parametros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    usuario_logado = Column(String)
    salvar_senha = Column(Integer)
    senha_salva = Column(String) 

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    usuario = Column(String)
    senha = Column(String)
    permissao = Column(String)

class Bancos(Base):
    __tablename__ ='bancos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    tipo = Column(String)

class ContasBancarias(Base):
    __tablename__ = 'contas_bancarias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    banco_id = Column(Integer, ForeignKey('bancos.id'))
    agencia = Column(String)
    conta = Column(String)
    saldo_inicial = Column(String)
    saldo_atual = Column(String)

class Despesas(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    descricao = Column(String)
    valor = Column(String)
    data_pag = Column(Date)
    data = Column(DateTime)
    data_lanc = Column(DateTime)
    
class Receitas(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    descricao = Column(String)
    valor = Column(String)
    data_pag = Column(Date)
    data = Column(DateTime)
    data_lanc = Column(DateTime)
    
class Investimentos(Base):
    __tablename__ = 'investimentos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    conta_id = Column(Integer,ForeignKey('contas_bancarias.id'))
    descricao = Column(String)
    data_abert = Column(DateTime)
    data_fech = Column(DateTime)    
    valor_inicial = Column(String)
    perc_valorizacao = Column(String)
    tipo_valorizacao = Column(String)
    banco = Column(Integer, ForeignKey("bancos.id"))
    conta_id = Column(Integer,ForeignKey("contas_bancarias.id"))
    
class MovimentacaoInvestimento(Base):
    __tablename__ = 'mov_investimento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    investimento_id = Column(Integer, ForeignKey("investimentos.id"))
    valor = Column(String)
    tipo = Column(String)
    descricao = Column(String)
    data = Column(DateTime)



if not os.path.exists(path_db):
   Base.metadata.create_all(bind=engine) 

def new_user(bussines:int,name:str, user:str,password:str, email:str ='', phone:str = '', permission:str =''):
    novo_usuario = Usuarios(empresa_id=bussines,nome=name,usuario=user,senha=password,email=email,telefone=phone,permissao=permission)
    session.add(novo_usuario)
    session.commit()
    pass

def get_user(type:str,name:str = None,user:str= None,id:int=None):
    match type:
        case "nome":
            return session.query(Usuarios).filter_by(nome = name).all()
        case "user":
            a = session.query(Usuarios).filter_by(usuario = user).all()
            for usuario in a:
                return usuario.nome, usuario.senha

        case "id":
            return session.query(Usuarios).filter_by(id = id).all()
        case "count": 
            return session.query(Usuarios).count()
        
        case "user_filter":
            return session.query(Usuarios).filter_by(usuario = user).count()
            
        
        case _:
            return session.query(Usuarios).all()
        


   

if __name__=='__main__':
   a =  get_user(type="user",user='juliosales')
   print(a)
  

          
    
               