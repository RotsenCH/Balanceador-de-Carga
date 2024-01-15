from flask import Flask, redirect

servidor3 = Flask(__name__)

@servidor3.route('/')
def hola():
    return redirect("https://www.linkedin.com/", code=302)


if __name__ == '__main__':
    servidor3.run(host='0.0.0.0')