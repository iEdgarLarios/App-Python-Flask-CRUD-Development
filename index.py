from flask import Flask, render_template, request
from controllers.crud import *

db = ""
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('insertdata.html')

@app.route('/messageinsertdata', methods=['POST'])
def showdatainsert():
    try:
        key = request.form['key']
        name = request.form['name']
        salary = request.form['salary']
        response = insertData(db, key, name, salary)
        if(response != False):
            return render_template("messageinsertdata.html")
        else:
            return render_template("error.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/showdata')
def showdata():
    try:
        response = showData(db)
        if(response != False):
            return render_template("showdata.html", tables=response)
        else:
            return render_template("error.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/searchdata')
def searchdata():
    try:
        return render_template("searchdata.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/showsearchdata', methods=['POST'])
def showsearchdata():
    try:
        name = request.form['name']
        response = searchData(db, name)
        if(response != False):
            return render_template("showsearchdata.html", name=response)
        else:
            return render_template("error.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/deletedata')
def deletedata():
    try:
        return render_template("deletedata.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/showdeletedata', methods=['POST'])
def showdeletedata():
    try:
        deleteData(db)
        return render_template("showdeletedata.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/modifydata')
def modifydata():
    try:
        return render_template("modifydata.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/showmodifydata', methods=['POST'])
def showmodifydata():
    try:
        key = request.form['key']
        name = request.form['name']
        response = updateData(db, key, name)
        if(response != False):
            return render_template("showmodifydata.html")
        else:
            return render_template("error.html")
    except SystemError as err:
        print(err)
        return render_template("error.html")

@app.route('/personaldata')
def personaldata():
    name = "Erika Yunuen Flores Monroy"
    age = 23
    subject = ["Inteligencia Artificial", "Programación", "Redes de computadoras"]
    return render_template('personaldata.html', name = name, age = age, subject = subject)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Página no encontrada</h1>"

if __name__ == '__main__':
    db = dbConnection()
    createTables(db)
    app.run(port=80, debug=True)