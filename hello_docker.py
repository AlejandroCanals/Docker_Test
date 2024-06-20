from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, este es mi primer contenedor con Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
