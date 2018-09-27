from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth')
def auth():
    user = request.args['username']
    method = request.method
    return render_template('auth.html', method=method, user=user)

if __name__ == '__main__':
    app.debug = True
    app.run()

