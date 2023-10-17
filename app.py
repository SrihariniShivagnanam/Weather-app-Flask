import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def render_results():
    city_name = request.form['city']
    print(city_name)

    api_key = "3c195f88f2b5332c421ae8dd55ae467e"
    data = get_weather_results(city_name, api_key)
    print(data)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html',
                           location=location, temp=temp,
                           feels_like=feels_like, weather=weather)


def get_weather_results(city, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(api_url)
    return r.json()


if __name__ == '__main__':
    app.run(debug=True)