"""A class of weather report."""
import pyowm




class Weather: #implemented class
    """ Class that gives the weather report.
    """

    def __init__(self, name):
        owm = pyowm.OWM('c56ba86f15e44e73a6e50e64c99b06df')
        self.three_hours_forecast = owm.three_hours_forecast("Berkeley,us")
        self.forecast = self.three_hours_forecast.get_forecast();
        self.today_weather_list = self.forecast.get_weathers()[:8]
        self.high_temp, self.high_temp_time = self.get_high_temp(self.today_weather_list)
        self.low_temp, self.low_temp_time = self.get_low_temp(self.today_weather_list)
        self.rain_dict = self.get_rain(self.today_weather_list)
        self.compose()    	


    def get_high_temp(self, weather_list):
        """ Gets the highest temperature among the WEATHER_LIST
        """
        max_temp = 0
        for weather in weather_list:
            temp = weather.get_temperature('fahrenheit')["temp_max"]
            if temp >= max_temp:
                max_temp = temp
                time = weather.get_reference_time('iso')[11:-3]

        return max_temp, time

    def get_low_temp(self, weather_list):
        """ Gets the lowest temperature among the WEATHER_LIST
        """
        min_temp = 999999
        for weather in weather_list:
            temp = weather.get_temperature('fahrenheit')["temp_min"]
            if temp <= min_temp:
                min_temp = temp
                time = weather.get_reference_time('iso')[11:-3]

        return min_temp, time

    def get_rain(self, weather_list):
        """ Returns a dictionary with rain status as keys and
            and raining time as values for the WEATHER_LIST
        """
        rain_dict = {}
        for weather in weather_list:
            if "rain" in weather.get_detailed_status():
                status = weather.get_detailed_status()
                time = weather.get_reference_time('iso')[11:-3]
                rain_dict[status] = time

        return rain_dict



    def compose(self): #fixme --> includes 5 days
        """ Composing a message to be sent to email.
        """
        msg = "\nToday, the high will be %sF around " \
              "%s and the low will be %sF around %s.\n" \
              % (self.high_temp, self.high_temp_time, \
               self.low_temp, self.low_temp_time)
        if not self.rain_dict:
            msg += "No rain today!"
        else:
            for item in self.rain_dict.items():
                msg += "There will be %s, at around %s." % (item[0], item[1])
        return msg
