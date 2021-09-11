from flask import Flask, render_template

app = Flask(__name__)

#Rutas o endpoints
#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
    #return '<h1>Hola mundo desde Flask 3</h1>'
    vehiculos=['mazda','renault','toyota','chevrolet','audi']
    
    datosindex = {
        'titulo': 'sistema de prueba',
        'subtitulo': 'Bienvenido al sistema, estimado usuario: ',
        'usuario': 'myTestName',
        'referencias': ['3','Logan','celica','aveo','A5'],
        'vehiculos': vehiculos,
        'cantVehiculos': len(vehiculos)
    }
    
    return render_template('index.html',data=datosindex)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(port=7000, debug=True)

