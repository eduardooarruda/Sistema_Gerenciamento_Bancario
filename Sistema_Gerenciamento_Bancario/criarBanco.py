from pathlib import Path
from unicodedata import name
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///banco.db' , echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, autoincrement=True, primary_key=True)
    numeroConta = Column(String(50))
    saldo = Column(Float)
    agencia = Column(String(5))
    chequeEspecial= Column(Boolean)
    valorChequeEspecial= Column(Float)
    nome = Column(String(50))
    cpf = Column(String(20))
    senha = Column(String(30))
    estado = Column(String(30))
    cidade = Column(String(30))
    bairro = Column(String(30))
    rua = Column(String(30))
    numeroEndereco = Column(String(30))
    data_criacao = Column(Date)
    data_atualizacao_rendimento_poupanca = Column(Date)
    extrato = relationship('Extrato', backref='conta', lazy=True, cascade="all, delete")

class Extrato(Base):
    __tablename__ = 'extrato'
    id = Column(Integer, autoincrement=True, primary_key=True)
    idConta = Column(Integer, ForeignKey('conta.id'), nullable=False)
    data = Column(Date)
    tipo_operacao = Column(String(20))
    saldo_anterior = Column(Float)
    saldo_novo = Column(Float)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
