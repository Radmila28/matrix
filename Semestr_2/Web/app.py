from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        r = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=af7d75d08bbfe9d73c57554c3fda716c')

        json_object = r.json()

        temperature = int(json_object['main']['temp'] - 273.15)
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        wind = int(json_object['wind']['speed'])

        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']

        return render_template('home.html', temperature=temperature, pressure=pressure, humidity=humidity,
                               city_name=city_name, condition=condition, wind=wind, desc=desc)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)