"""A Reader for 5-day forecaster in JSON type """
import json
import urllib.request


##################################################
# Static Variables
API_KEY = 'c56ba86f15e44e73a6e50e64c99b06df'
WEATHER_LIST_KEY = 'list'

#####################################################
# Class Definitions

class JsonForecastReader:
	""" Class that reads the 5-day forecast from OWM
	"""

	def __init__(self, cityName, countryCode="us", unit="imperial"):
		""" Constrcutor wich takes in CITYNAME and UNIT
			UNIT - 'imperial' uses Fahrenheit; 'metric' uses Celcius
		"""
		self.cityName = cityName
		self.countryCode = countryCode
		self.unit = unit


	def getDataDict(self):
		apiUrl = "http://api.openweathermap.org/data/2.5/forecast?\
		q={},{}&mode=JSON&units={}&APPID={}".format(self.cityName,\
					 self.countryCode, self.unit, API_KEY)
		with urllib.request.urlopen(apiUrl) as response:
			jsonData = response.read().decode('utf-8')
		
		return json.loads(jsonData) 


	def getWeatherList(self):
		return self.getDataDict().get(WEATHER_LIST_KEY)

