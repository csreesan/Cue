"""A class of weather report."""
from Weather import Weather, TODAY


class WeatherMessage:
    """ Class that gives the weather report.
    """

    def __init__(self, cityName, coutnryCode="us", unit="imperial"):
        self.weather = Weather(cityName, coutnryCode, unit)	


    def getHighTempAndTime(self):
        """ Gets the highest temperature among the WEATHER_LIST
        """
        return self.weather.getDayMaxTempAndTime(TODAY)


    def getLowTempAndTime(self):
        """ Gets the lowest temperature among the WEATHER_LIST
        """
        return self.weather.getDayMinTempAndTime(TODAY)

    def getRainAndTime(self):
        """ Returns a list of tuple with rain status as keys and
            and raining time as values for the WEATHER_LIST
        """
        return self.weather.getDayRainDesAndTime(TODAY)



    def compose(self): #fixme --> includes 5 days
        """ Composing a message to be sent to email.
        """
        msg = "\nToday, the high will be %sF around " \
              "%s and the low will be %sF around %s.\n" \
              % (self.getHighTempAndTime()[0], self.getHighTempAndTime()[1],\
                self.getLowTempAndTime()[0], self.getLowTempAndTime()[1])
        if not self.getRainAndTime():
            msg += "No rain today!"
        else:
            for rainAndTimeTuple in self.getRainAndTime():
                msg += "There will be %s, at around %s." % (rainAndTimeTuple[0],\
                 rainAndTimeTuple[1])
        return msg
