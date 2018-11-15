import json
import urllib.request
from flask import Flask, render_template
import util.conf

app = Flask(__name__)
conf_file = 'data/app.json'

@app.route('/')
def index():
    KEY = 'NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo'
    url = util.conf.get_base_url()
    with urllib.request.urlopen(url) as f:
        result = json.loads(f.read())
    #  pic = result['url']
    return render_template('index.html', test=str(result))

if __name__ == '__main__':
    app.debug = True
    app.run()

