import sqlite3

#создаем подключение к базе данных (файл называется "my_database.db")
connection=sqlite3.connect('my_database.db')
cursor = connection.cursor()
def productBD():
    listDB=cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

if __name__ =='__main__':
    print(productBD())