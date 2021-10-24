from flask import Flask,render_template, request, flash,redirect

import mysql.connector

app = Flask(__name__)

app.secret_key='mysecretkey'




@app.route('/')
def inicio():

    return render_template('index.html')


@app.route('/listar',methods=['POST'])
def coneccion():
    port=request.form['port']
    DB = mysql.connector.connect(
        host=request.form['hostname'],
        user=request.form['user'],
        password=request.form['contrasena'],
        port=port
    )
    cursor = DB.cursor(dictionary=True)
    cursor.execute('SHOW DATABASES')
    listado=cursor.fetchall()
    flash('Listado de bases de datos generada exitosamente')
    return render_template('index.html',bases=listado)


@app.get('/nuevo')
def crearnuevo():

    return render_template('crear.html')


@app.route('/crear',methods=['POST'])
def crearBase():
    port=request.form['port']
    nombre= request.form['nombre']
    DB = mysql.connector.connect(
        host=request.form['hostname'],
        user=request.form['user'],
        password=request.form['contrasena'],
        port=port
    )
    cursor = DB.cursor(dictionary=True)
    cursor.execute(f"CREATE DATABASE {nombre}")
    DB.commit()
    cursor.close()
    flash('Base de datos creada exitosamente')
    return redirect('/nuevo')

app.run(debug=True)
