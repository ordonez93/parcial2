from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
app= Flask(__name__)

@app.get('/')
def inicio():
    return render_template('index.html')
 

app.run(debug=True)