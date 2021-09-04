from flask import Flask

app = Flask(__name__)

#Rutas o endpoints
#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
    return '<h1>Hola mundo desde Flask 3</h1>'

if __name__ == "__main__":
    	app.run(port=7000, debug=True)

