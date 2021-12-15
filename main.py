from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la petición")

@app.after_request
def after_request(response):
    print("Después de la petición")
    return response


@app.route('/')
def index():
    name = "Rafa"
    curso = "Python Web"
    is_premium = True
    cursos = ['Python', 'Ruby', 'Java', 'Elixir']

    return render_template('index.html', username=name, nombre_curso=curso, premium=is_premium, cursos=cursos)

@app.route('/about')
def about():
    print("Estamos en el about")
    return render_template('about.html')

def suma(val1, val2):
    return val1 + val2

@app.route('/suma')
def suma_template():
    return render_template('suma.html', val1=15, val2=20, funcion=suma)


@app.route('/usuario/<last_name>/<name>/<int:age>')
def usuario(last_name, name, age):
    return 'Hola ' + last_name + ' ' + name + ' ' + str(age)


@app.route('/datos')
def datos():
    nombre = request.args.get('nombre')  # args devuelve un diccionario
    curso = request.args.get('curso')
    return 'Listado de datos: ' + nombre + ' ' + curso

if __name__ == '__main__':
    app.run(debug=True)