from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask!</h1>'
@app.route('/user/<id>')
def user(id):
    return '<h1>Hello, %s!' % id
if __name__ == '__main__':
    app.run(debug=True)
