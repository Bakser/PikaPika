from flask import Flask,url_for
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    url_for('static',filename='miserables.json')
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
   return render_template('hello.html', name=name)

@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
