from flask import Flask

servidor5 = Flask(__name__)

@servidor5.route('/')
def hola():
    return "Hola desde servidor 5"

if __name__ == '__main__':
    servidor5.run(host='0.0.0.0')