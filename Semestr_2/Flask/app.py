from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    t = soup.find('div',  id = "weather-now-number").getText()
    return render_template(('index.html'), t = t)


if __name__ == '__main__':
    app.run(debug=True)
