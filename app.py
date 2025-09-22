from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

#создаем подключение к базе данных (файл называется "my_database.db")
connection=sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

def productBD():
    listDB=cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

@app.route("/")
def index():
    shop= productBD()
    return render_template("index.html", shop=shop)



@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/search")#Поиск
def search():
    return render_template("search.html")

@app.route("/login") #Вход в аккаунт/Регистрация
def login():
    return render_template("login.html")


@app.route("/about")#о нас
def about():
    return render_template('about.html')

@app.route("/news")#новости и акции
def news():
    return render_template('news.html')

if __name__ =='__main__': #точка ввода нашей программы
    print("Сервер запущен:")
    app.run(debug=True)