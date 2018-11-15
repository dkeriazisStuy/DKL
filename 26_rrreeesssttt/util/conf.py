import json

CONF_FILE = 'data/conf.json'

def get_base_url():
    """Returns the base url for the Dark Sky API"""
    with open(CONF_FILE) as f:
        result = json.load(f)
    url = 'https://api.darksky.net/forecast/{key}/{lat},{lon}'.format(
            key=result['key'],
            lat=result['lat'],
            lon=result['long']
    )
    return url

