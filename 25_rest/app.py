import json
import urllib.request
from flask import Flask, render_template
import util.conf

app = Flask(__name__)
conf_file = 'data/app.json'

@app.route('/')
def index():
    url = util.conf.get_base_url()
    print(url)
    with urllib.request.urlopen(url) as f:
        result = json.loads(f.read())
    icon = result['currently']['icon']
    icon_map = {
        'clear-day': 'far fa-sun',
        'clear-night': 'far fa-moon',
        'rain': 'fas fa-cloud-rain',
        'snow': 'fas fa-slowflake',
        'sleet': 'fas fa-slowflake',
        'wind': 'fas fa-wind',
        'fog': 'fas fa-smog',
        'cloudy': 'fas fa-cloud',
        'partly-cloudy-day': 'fas fa-cloud-sun',
        'partly-cloudy-night': 'fas fa-cloud-moon',
    }
    if icon in icon_map:
        favicon = icon_map[icon]
    else:
        favicon = 'fas fa-question'
    summary = result['currently']['summary']
    temp = result['currently']['temperature']
    temp = round(temp, 1)
    apparentTemp = result['currently']['apparentTemperature']
    low = result['daily']['data'][0]['temperatureLow']
    high = result['daily']['data'][0]['temperatureHigh']
    alerts = result['alerts']
    return render_template(
        'index.html',
        favicon=favicon,
        summary=summary,
        temp=temp,
        apparentTemp=apparentTemp,
        low=low,
        high=high,
        alerts=alerts,
    )

if __name__ == '__main__':
    app.debug = True
    app.run()

