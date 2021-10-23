from flask import Flask, render_template, request, redirect, flash
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import response
from controllers import dataBases

app= Flask(__name__)

@app.get('/')
def home():
    
    return render_template('index.html')


@app.get('/listar')
def listar():
    home(render_template('index.html'))
    data = request.form

    DB = dataBases.coneccion(
        host=data["hostname"],
        user=data["usuario"],
        password=data["contrasena"],
        port=data["puerto"]
    )
    verbases = dataBases.getDatabases(DB)
    return render_template('listar.html',Bases=verbases)
 
@app.post('/crear')
def crearBase():
   data = request.form
   
    DB = dataBases.coneccion(
        host=data["hostname"],
        user=data["usuario"],
        password=data["contrasena"],
        port=data["puerto"],
    )
    nombre=data["nombre"]
    nuevo = dataBases.crearBase(DB,nombre)
    return render_template('index.html',nuevo)


app.run(debug=True)