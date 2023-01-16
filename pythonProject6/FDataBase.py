import sqlite3
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getMenu(self):
        sql = '''SELECT * FROM Users'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
             print("Ошибка чтения из БД")
        return []


    def addUser(self, FullName, Login, Password):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM Users WHERE '{Login}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким логином уже существует")
                return False
            self.__cur.execute("INSERT INTO Users VALUES(NULL, ?, ?, ?, ?, ?)", (FullName, Login, Password))
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя"+str(e))
            return False

        return True