from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

__all__ = ['Base', 'session']

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}:{port}/{databasename}?charset=utf8".format(
    username="root",
    password="sm1418!1662",
    hostname="192.168.0.13",
    port="3306",
    databasename="jeongain"
)

#데이터 베이스에 접속한다.
DATABASES = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base()

# Database를 없으면 생성
Base.metadata.create_all(DATABASES)

# 세션을 만들어서 연결시킨다.
Session = sessionmaker()
Session.configure(bind=DATABASES)
session = Session()
