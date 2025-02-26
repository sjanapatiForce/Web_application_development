from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"
@app.route('/hello/<userName>')
def hello(userName):
    return (f'hello there, {userName}!')

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)