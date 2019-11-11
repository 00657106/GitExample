from flask import *
from datetime import datetime
import calculate
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return render_template('index.html')

@app.route('/add')
def add():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculate.add(a,b))

@app.route('/decrease')
def decrease():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculate.minus(a,b))

@app.route('/multiply')
def multiply():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculate.times(a,b))

@app.route('/divide')
def divide():
    a = num(request.args.get('a'))
    b = num(request.args.get('b'))
    return str(calculate.divided(a,b))


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    app.run(debug=True)