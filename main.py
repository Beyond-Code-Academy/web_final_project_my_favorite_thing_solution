from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)


@web_site.route('/')
def index():
	return render_template('index.html')


@web_site.route('/Consoles')
def Consoles():
	return render_template('Consoles.html')

@web_site.route('/Games')
def Games():
	return render_template('Games.html')



web_site.run(host='0.0.0.0', port=8080)