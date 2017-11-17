from ForecastReader import JsonForecastReader
from collections import OrderedDict




##################################################
# Static Variables
# Day keys
TODAY = 'today'
DAY_2 = 'day2'
DAY_3 = 'day3'
DAY_4 = 'day4'
DAY_5 = 'day5'

# Weather list index
TODAY_END = 4
DAY_LIST_NUM = 8
DAY_2_END = TODAY_END + DAY_LIST_NUM
DAY_3_END = DAY_2_END + DAY_LIST_NUM
DAY_4_END = DAY_3_END + DAY_LIST_NUM
DAY_5_END = DAY_4_END + DAY_LIST_NUM

# Weather list keys
DATE_TIME_KEY = 'dt_txt'
WEATHER_KEY = 'weather'
RAIN_KEY = 'rain'
MAIN_TEMP_KEY = 'main'

# All keys for specific temperatures
TEMP_KEY = 'temp'
MAX_TEMP_KEY = 'temp_max'
MIN_TEMP_KEY = 'temp_min'

# Weather dict key
WEATHER_DESCRIPTION_KEY = 'description'

# Initial Min and Max Temp
INIT_MIN_TEMP = 99999
INIT_MAX_TEMP = -99999


#####################################################
# Class Definitions

class Weather:
    """ Class representing weather objects
    """

    def __init__(self, cityName, countryCode="us", unit="imperial"):

        self.forecastReader = JsonForecastReader(cityName, countryCode, unit)
        self.weatherList = self.forecastReader.getWeatherList()
        self.daysDict = self.getDaysDict()


    def getDaysDict(self):
        """ get days dict
        """
        daysDict = OrderedDict()
        daysDict[TODAY] = Day(self.weatherList[:TODAY_END])
        daysDict[DAY_2] = Day(self.weatherList[TODAY_END:DAY_2_END])
        daysDict[DAY_3] = Day(self.weatherList[DAY_2_END:DAY_3_END])
        daysDict[DAY_4] = Day(self.weatherList[DAY_3_END:DAY_4_END])
        daysDict[DAY_5] = Day(self.weatherList[DAY_4_END:DAY_5_END])
        return daysDict


    def getDayFromString(self, dayString):
        return self.daysDict[dayString]


    def getDayMaxTempAndTime(self, dayString):
        day = self.getDayFromString(dayString)
        return day.getMaxTempAndTime()


    def getDayMinTempAndTime(self, dayString):
        day = self.getDayFromString(dayString)
        return day.getMinTempAndTime()


    def getDayRainDesAndTime(self, dayString):
        day = self.getDayFromString(dayString)
        return day.getRainDesAndTimeTupleList()

    def getSpecificWeatherDes(self, dayString, timeString):
        day = self.getDayFromString(dayString)
        return day.getTimeObject(timeString).getWeatherDes()

    def getSpecificMaxTemp(self, day, time):
        day = self.getDayFromString(dayString)
        return day.getTimeObject(timeString).getMaxTemp()

    def getSpecificMinTemp(self, dayString, time):
        day = self.getDayFromString(dayString)
        return day.getTimeObject(timeString).getMinTemp()



class Day:
    """ Class represeting the Day
    """

    def __init__(self, dayDataList):
        self.date = self.getDataDate(dayDataList[0])
        self.dayDataList = dayDataList
        self.timesDict = self.getTimesDict()

    def getDate(self):
        return self.date


    def getTimeObject(self, time):
        return self.timesDict[time]


    def getDataDate(self, dataDict):
        return dataDict.get(DATE_TIME_KEY)[0:10]

    def getDataTime(self, dataDict):
        return dataDict.get(DATE_TIME_KEY)[11:]

    def getTimesDict(self):
        timesDict = OrderedDict()
        for timeDataDict in self.dayDataList:
            assert self.getDataDate(timeDataDict) == self.date, "Can't have different dates yo!"
            timesDict[self.getDataTime(timeDataDict)] = Time(timeDataDict)
        return timesDict

    def getMaxTempAndTime(self):
        maxTemp = INIT_MAX_TEMP
        maxTempTime = None
        for time in self.timesDict.keys():
            temp = self.getTimeObject(time).getTemp()
            if temp >= maxTemp:
                maxTemp = temp
                maxTempTime = time

        return maxTemp, maxTempTime


    def getMinTempAndTime(self):
        minTemp = INIT_MIN_TEMP
        minTempTime = None
        for time in self.timesDict.keys():
            temp = self.getTimeObject(time).getTemp()
            if temp <= minTemp:
                minTemp = temp
                minTempTime = time

        return minTemp, minTempTime

    def getRainDesAndTimeTupleList(self):
        lst = []
        for time in self.timesDict.keys():
            weatherDes = self.getTimeObject(time).getWeatherDes()
            if "rain" in weatherDes:
                lst.append((weatherDes, time))
        return lst




class Time:
    """ Class
    """
    def __init__(self, timeDataDict):
        self.timeDataDict = timeDataDict
        self.time = self.getDataTime()

    def getTime(self):
        return self.time

    def getDataTime(self):
        return self.timeDataDict.get(DATE_TIME_KEY)[11:]

    def getTemp(self):
        return self.timeDataDict.get(MAIN_TEMP_KEY).get(TEMP_KEY)

    def getMaxTemp(self):
        return self.timeDataDict.get(MAIN_TEMP_KEY).get(MAX_TEMP_KEY)

    def getMinTemp(self):
        return self.timeDataDict.get(MAIN_TEMP_KEY).get(MIN_TEMP_KEY)

    def getWeatherDes(self):
        return self.timeDataDict.get(WEATHER_KEY)[0].get(WEATHER_DESCRIPTION_KEY)

