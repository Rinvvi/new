from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=['post','get'])
def integer():
    messege = ''
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        messege = messege+user + ' ' + password
        return render_template('proba.html',messege = messege)

    return render_template("proba.html",messege='Форма')

if __name__=='__main__':
    print("run server")
    app.run()