from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker



engine = create_engine("sqlite:///test.db", echo = True)#1 шаг указываем с какой базой данных мы работаем
base = declarative_base()#2 шаг объявляем раскладку базы
sesion = sessionmaker(bind=engine)() # 4 шаг Созадние сессии с базой данных

class Users(base):  # 3 шаг создание класса таблицы
    __tablename__ = "users"#Задаем таблицы название

    #Создаем колонки
    uid = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

def create_user(data):
    created_user = Users(name = data["name"],full_name = data["full_name"])#5 шаг создание пользователя
    sesion.add(created_user) # Добавление пользователя в сессию
    sesion.commit() # Синхронизация с сессией базой данных


while True:
    name = input("Введите имя: ")
    full = input("Введите фамилию: ")
    create_user({"name": name, "full_name" : full})
# base.metadata.create_all(engine) # Команда для создание базы данных
