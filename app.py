from flask import Flask
import requests
import time
import os

app = Flask(__name__, static_folder=os.path.abspath('./'))

API_KEY = "b6907d289e10d714a6e88b30761fae22"

@app.route('/')
def index():
    page = app.send_static_file('index.html')
    return page

@app.route('/&lt;string:city&gt;/&lt;string:country&gt;/')
def weather_by_city(country, city):

    url = 'https://samples.openweathermap.org/data/2.5/weather'
    params = dict(
        q=city + "," + country,
        appid= API_KEY,
    )

    response = requests.get(url=url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
