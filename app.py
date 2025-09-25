from flask import Flask
from flask import render_template,request
import sqlite3

app = Flask(__name__)

#создаем подключение к базе данных (файл называется "my_database.db")
connection=sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

def productDB():
    listDB=cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def product_oneDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

def product_twoDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

def product_accessoriesDB(id):
    listDB=cursor.execute('SELECT * FROM product where category="'+id+'"')
    return listDB.fetchall()

@app.route("/")
def index():
    shop= productDB()
    return render_template("index.html", shop=shop)



@app.route("/shop")
def shop():
    shop= productDB()
    return render_template("shop.html", shop=shop)

@app.route("/cat/<id>")
def boots(id):
    shop= product_accessoriesDB(id)
    product_accessoriesDB
    return render_template("boots.html", shop=shop)

@app.route("/cat/<id>")
def accessories(id):
    shop= product_accessoriesDB(id)
    product_accessoriesDB
    return render_template("accessories.html", shop=shop)


@app.route("/search/<id>")#Поиск
def search(id):
    shop= product_twoDB(id)
    print(index)
    return render_template("search.html",shop=shop)
    

@app.route("/proba") #Вход в аккаунт/Регистрация
def proba():
    return render_template("proba.html")


@app.route("/about")#о нас
def about():
    return render_template('about.html')

@app.route("/basket/<id>" )#корзина
def basket(id):
    shop= product_oneDB(id)
    print(shop)
    return render_template('basket.html', shop=shop)

@app.route("/news")#новости и акции
def news():
    shop= productDB()
    return render_template('news.html', shop=shop)



if __name__ =='__main__': #точка ввода нашей программы
    print("Сервер запущен:")
    app.run(debug=True)