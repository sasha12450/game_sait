from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine("sqlite:///test.db", echo=True)
session = sessionmaker(bind=engine)()
base = declarative_base()
class User(base):
    __tablename__ = 'Users'
    uid = Column(Integer, primary_key=True)
    name = Column(String )
class Chats(base):
    __tablename__ = 'Chats_message'
    uid = Column(Integer, primary_key=True)
    from_id = Column(Integer)
    to_id = Column(Integer)
    time = Column(String)
    text = Column(String)

# polzovatel = User(name='Вася')
# polzovatel2 = User(name='Петя')
# session.add_all([polzovatel, polzovatel2])
# session.commit()
# while True:
#     message1=input("Вася вводит сообщение: ")
#     message2=input("Петя вводит сообщение: ")
#     mes1= Chats(from_id = 1, to_id = 2, text= message1, time = datetime.now())
#     mes2= Chats(from_id = 2, to_id = 1, text= message2, time = datetime.now())
#     session.add_all([mes1, mes2])
#     session.commit()
# base.metadata.create_all(engine)


query1 = session.query(Chats).filter_by(from_id = 1, to_id = 2).all()
query2 = session.query(Chats).filter_by(from_id = 2, to_id = 1).all()
query1.extend(query2)
query1 = sorted(query1, key=lambda mes: mes.time)
for mes in query1:
    print(mes.from_id, mes.text)



