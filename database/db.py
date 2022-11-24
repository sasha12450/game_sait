import sqlite3




def conection(sql):
    with sqlite3.connect("sait.db") as conect:
        kursor = conect.cursor()
        kursor.execute(sql)
        return kursor.fetchall()
def create_user_table():
    qery="""
    CREATE TABLE users_table(
     uid INTEGER PRIMARY KEY AUTOINCREMENT,
     user_name NVARCHAR(20) NOT NULL,
     email VARCHAR NOT NULL,
     password NVARCHAR NOT NULL,
     grade INTEGER
     CONSTRAINT grade DEFAULT 0)
    """
    conection(qery)
def create_ad_table():
    qery = """
        CREATE TABLE add_table(
         uid INTEGER PRIMARY KEY AUTOINCREMENT,
         trader_id INTEGER NOT NULL,
         short_desc NVARCHAR(70),
         full_desc NVARCHAR(400),
         type_ad NVARCHAR NOT NULL,
         type_bust NVARCHAR CONSTRAINT type_bust DEFAULT none,
         type_LBZ NVARCHAR CONSTRAINT type_LBZ DEFAULT none,
          NVARCHAR NOT NULL,
          INTEGER CONSTRAINT fights_count DEFAULT 0,
         win_rait INTEGER CONSTRAINT win_rait DEFAULT 0,
          INTEGER CONSTRAINT rait DEFAULT 0,
          INTEGER CONSTRAINT wn8 DEFAULT 0,
        INTEGER CONSTRAINT count DEFAULT 0,
         price INTEGER CONSTRAINT price DEFAULT 0,
         is_active BIT CONSTRAINT is_active DEFAULT 1,
         FOREIGN KEY (trader_id) REFERENCES users_table(uid))
        """
    conection(qery)




def add_user(data):
    qery = f"""
    INSERT INTO users_table(user_name, email, password)
    VALUES ('{data['user_name']}', '{data['email']}', '{data['password']}')
    """
    conection(qery)
def check_exists(data):
    qery = f"""
    SELECT * FROM users_table
    """
    db_data = conection(qery)
    for user in db_data:
        print(user)
        if user[0] == data['user_name'] or user[1] == data['email']:
            return True
    return False






if __name__ == "__main__":
    check_exists({"user_name": "test",
              "email":"test@mail.ru",
              "password":"123456667"})
