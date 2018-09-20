from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/foo')
def foo():
    return '<b>Is this text bold?</b>'

@app.route('/bar')
def bar():
    return '''<a href="/">Back to index!</a><br>
              <a href="/foo">Go to foo!</a>'''

if __name__ == "__main__":
    app.debug = True
    app.run()
