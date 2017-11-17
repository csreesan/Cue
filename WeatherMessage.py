"""A class of weather report."""
from Weather import Weather


class WeatherMessage:
    """ Class that gives the weather report.
    """

    def __init__(self, cityName, coutnryCode="us", unit="imperial"):
        self.weather = Weather(cityName, coutnryCode, unit)	


    def getHighTempAndTime(self, weather_list):
        """ Gets the highest temperature among the WEATHER_LIST
        """
        return self.weather.getDayMaxTempAndTime(Weather.TODAY)


    def getLowTempAndTime(self, weather_list):
        """ Gets the lowest temperature among the WEATHER_LIST
        """
        return self.weather.getDayMinTempAndTime(Weather.TODAY)

    def getRainAndTime(self, weather_list):
        """ Returns a list of tuple with rain status as keys and
            and raining time as values for the WEATHER_LIST
        """
        return self.weather.getDayRainDesAndTime(Weather.TODAY)



    def compose(self): #fixme --> includes 5 days
        """ Composing a message to be sent to email.
        """
        msg = "\nToday, the high will be %sF around " \
              "%s and the low will be %sF around %s.\n" \
              % (self.high_temp, self.high_temp_time, \
               self.low_temp, self.low_temp_time)
        if not self.getRainAndTime:
            msg += "No rain today!"
        else:
            for rainAndTimeTuple in self.getRainAndTime:
                msg += "There will be %s, at around %s." % (rainAndTimeTuple[0],\
                 rainAndTimeTuple[1])
        return msg
