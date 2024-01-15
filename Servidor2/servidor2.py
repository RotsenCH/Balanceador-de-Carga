from flask import Flask, redirect

servidor2 = Flask(__name__)

@servidor2.route('/')
def hola():
    return redirect("https://github.com/", code=302)

if __name__ == '__main__':
    servidor2.run(host='0.0.0.0')