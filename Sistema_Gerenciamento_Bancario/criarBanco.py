from datetime import datetime
from enum import unique
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class ContaCorrente(Base):
    __tablename__ = 'contaCorrente'
    id = Column(Integer, autoincrement=True, primary_key=True)
    numeroConta = Column(String(50), nullable=False, unique=True)
    saldo = Column(Float)
    agencia = Column(String(5))
    valorChequeEspecial = Column(Float)
    nome = Column(String(50))
    cpf = Column(String(20))
    senha = Column(String(30))
    estado = Column(String(30))
    cidade = Column(String(30))
    bairro = Column(String(30))
    rua = Column(String(30))
    numeroEndereco = Column(String(30))
    data_criacao = Column(DateTime)
    extrato = relationship(
        'ExtratoContaCorrente', backref='contaCorrente', lazy=True, cascade="all, delete")
    emprestimo = relationship(
        'EmprestimoContaCorrente', backref='contaCorrente', lazy=True, cascade="all, delete")

class ExtratoContaCorrente(Base):
    __tablename__ = 'extratoContaCorrente'
    id = Column(Integer, autoincrement=True, primary_key=True)
    idConta = Column(Integer, ForeignKey('contaCorrente.id'), nullable=False)
    data = Column(DateTime)
    tipo_operacao = Column(String(20))
    saldo_anterior = Column(Float)
    saldo_novo = Column(Float)
    

class EmprestimoContaCorrente(Base):
    __tablename__ = 'emprestimoContaCorrente'
    id = Column(Integer, autoincrement=True, primary_key=True)
    id_conta_corrente = Column(Integer, ForeignKey('contaCorrente.id'), nullable=False)
    valor = Column(Float)
    taxa = Column(Float)
    data = Column(DateTime)

class ContaPoupanca(Base):
    __tablename__ = 'contaPoupanca'
    id = Column(Integer, autoincrement=True, primary_key=True)
    numeroConta = Column(String(50))
    saldo = Column(Float)
    agencia = Column(String(5))
    valorChequeEspecial = Column(Float)
    nome = Column(String(50))
    cpf = Column(String(20))
    senha = Column(String(30))
    estado = Column(String(30))
    cidade = Column(String(30))
    bairro = Column(String(30))
    rua = Column(String(30))
    numeroEndereco = Column(String(30))
    data_criacao = Column(DateTime)
    data_atualizacao_rendimento_poupanca = Column(DateTime)
    extrato = relationship(
        'ExtratoContaPoupanca', backref='contaPoupanca', lazy=True, cascade="all, delete")
    emprestimo = relationship(
        'EmprestimoContaPoupanca', backref='contaPoupanca', lazy=True, cascade="all, delete")


class ExtratoContaPoupanca(Base):
    __tablename__ = 'extratoContaPoupanca'
    id = Column(Integer, autoincrement=True, primary_key=True)
    idConta = Column(Integer, ForeignKey('contaPoupanca.id'), nullable=False)
    data = Column(DateTime)
    tipo_operacao = Column(String(20))
    saldo_anterior = Column(Float)
    saldo_novo = Column(Float)

class EmprestimoContaPoupanca(Base):
    __tablename__ = 'emprestimoContaPoupanca'
    id = Column(Integer, autoincrement=True, primary_key=True)
    id_conta_poupanca = Column(Integer, ForeignKey('contaPoupanca.id'), nullable=False)
    valor = Column(Float)
    taxa = Column(Float)
    data = Column(DateTime)

class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer, autoincrement=True, primary_key=True)
    numeroContaCorrente = Column(String(50), ForeignKey('contaCorrente.numeroConta'), nullable=False)
    nome = Column(String(100))
    cargo_atual = Column(String(100))
    salario = Column(Float)
    jornada = Column(String(100))
    numero = Column(String(50))
    data_adimissao = Column(DateTime)
    beneficios = relationship(
        'Beneficios', backref='Funcionario', lazy=True, cascade="all, delete")

class Beneficios(Base):
    __tablename__ = 'Beneficios'
    id = Column(Integer, autoincrement=True, primary_key=True)
    id_funcionario = Column(Integer, ForeignKey('funcionario.id'), nullable=False)
    nome = Column(String(100))
    valor = Column(Float)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
