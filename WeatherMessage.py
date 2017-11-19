"""A class of weather report."""
from Weather import Weather, TODAY


class WeatherMessage:
    """ Class that gives the weather report.
    """

    def __init__(self, city_name, country_code="us", unit="imperial"):
        self.weather = Weather(city_name, country_code, unit)	

    def get_high_temp_and_time(self):
        """ Gets the highest temperature among the WEATHER_LIST
        """
        return self.weather.get_day_max_temp_and_time(TODAY)

    def get_low_temp_and_time(self):
        """ Gets the lowest temperature among the WEATHER_LIST
        """
        return self.weather.get_day_min_temp_and_time(TODAY)

    def get_rain_and_time(self):
        """ Returns a list of tuple with rain status as keys and
            and raining time as values for the WEATHER_LIST
        """
        return self.weather.get_day_rain_description_and_time(TODAY)

    def compose(self): ##fixme --> includes 5 days
        """ Composing a message to be sent to email.
        """
        d = u'\N{DEGREE SIGN}'

        msg = "\nToday, the high will be %s%sF around " \
              "%s and the low will be %s%sF around %s.\n" \
              % (self.get_high_temp_and_time()[0], d, self.get_high_temp_and_time()[1],
                 self.get_low_temp_and_time()[0], d, self.get_low_temp_and_time()[1])
        if not self.get_rain_and_time():
            msg += "No rain today!"
        else:
            for rain_and_time in self.get_rain_and_time():
                msg += "There will be %s, at around %s." % (rain_and_time[0],
                                                            rain_and_time[1])
        return msg
