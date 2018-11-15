import json
import urllib.request
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    KEY = 'NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo'
    url = 'https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&api_key={key}'.format(key=KEY)
    with urllib.request.urlopen(url) as f:
        result = json.loads(f.read())
    pic = result['url']
    return render_template('index.html', pic=pic)

if __name__ == '__main__':
    app.debug = True
    app.run()

