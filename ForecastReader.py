"""A Reader for 5-day forecaster in JSON type """
import json
import urllib.request
import urllib.parse


##################################################
# Static Variables
URL = 'http://api.openweathermap.org/data/2.5/forecast?'
API_KEY = 'c56ba86f15e44e73a6e50e64c99b06df'
WEATHER_LIST_KEY = 'list'

#####################################################
# Class Definitions


class JsonForecastReader:
	""" Class that reads the 5-day forecast from OWM
	"""

	def __init__(self, city_name, country_code="us", unit="imperial"):
		""" Constrcutor wich takes in CITYNAME and UNIT
			UNIT - 'imperial' uses Fahrenheit; 'metric' uses Celcius
		"""
		self.city_name = city_name
		self.country_code = country_code
		self.unit = unit

	def get_url_param_string(self):
		param_dict = {}
		param_dict['q'] = self.city_name + ',' + self.country_code
		param_dict['units'] = self.unit
		param_dict['mode'] = 'JSON'
		param_dict['APPID'] = API_KEY
		return urllib.parse.urlencode(param_dict)


	def getDataDict(self):
		full_url = URL + self.get_url_param_string()
		with urllib.request.urlopen(full_url) as response:
			json_string = response.read().decode()
		
		return json.loads(json_string) 


	def getWeatherList(self):
		return self.getDataDict().get(WEATHER_LIST_KEY)

