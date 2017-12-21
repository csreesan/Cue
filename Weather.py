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
TODAY_END = 5
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

    def __init__(self, city_name, country_code="us", unit="imperial"):

        self.forecast_reader = JsonForecastReader(city_name, country_code, unit)
        self.weather_list = self.forecast_reader.getWeatherList()
        #print(self.weather_list[0])
        self.days_dict = self.get_days_dict()
        
    def get_days_dict(self):
        """ get days dict
        """
        days_dict = OrderedDict()
        days_dict[TODAY] = Day(self.weather_list[:TODAY_END])
        days_dict[DAY_2] = Day(self.weather_list[TODAY_END:DAY_2_END])
        days_dict[DAY_3] = Day(self.weather_list[DAY_2_END:DAY_3_END])
        days_dict[DAY_4] = Day(self.weather_list[DAY_3_END:DAY_4_END])
        days_dict[DAY_5] = Day(self.weather_list[DAY_4_END:DAY_5_END])
        return days_dict

    def get_day_from_string(self, day_string):
        return self.days_dict[day_string]

    def get_day_max_temp_and_time(self, day_string):
        day = self.get_day_from_string(day_string)
        return day.get_max_temp_and_time()

    def get_day_min_temp_and_time(self, day_string):
        day = self.get_day_from_string(day_string)
        return day.get_min_temp_and_time()

    def get_day_rain_description_and_time(self, day_string):
        day = self.get_day_from_string(day_string)
        return day.get_rain_description_and_time_tuple_list()

    def get_time_weather_description(self, day_string, time_string):
        day = self.get_day_from_string(day_string)
        return day.get_time_object(time_string).get_weather_description()

    def get_time_max_temp(self, day_string, time_string):
        day = self.get_day_from_string(day_string)
        return day.get_time_object(time_string).get_max_temp()

    def get_time_min_temp(self, day_string, time_string):
        day = self.get_day_from_string(day_string)
        return day.get_time_object(time_string).get_min_temp()


class Day:
    """ Class representing the Day
    """

    def __init__(self, day_data_list):
        self.date = self.get_data_date(day_data_list[0])
        self.day_data_list = day_data_list
        self.times_dict = self.get_times_dict()

    def get_date(self):
        return self.date

    def get_time_object(self, time):
        return self.times_dict[time]

    @staticmethod
    def get_data_date(data_dict):
        return data_dict.get(DATE_TIME_KEY)[0:10]
    
    @staticmethod
    def get_data_time(data_dict):
        return data_dict.get(DATE_TIME_KEY)[11:]

    def get_times_dict(self):
        times_dict = OrderedDict()
        for time_data_dict in self.day_data_list:
            #print(self.get_data_time(time_data_dict))
            #print(self.get_data_date(time_data_dict), 'vs', self.date)
            assert self.get_data_date(time_data_dict) == self.date, "Can't have different dates yo!"
            times_dict[self.get_data_time(time_data_dict)] = Time(time_data_dict)
        return times_dict

    def get_max_temp_and_time(self):
        max_temp = INIT_MAX_TEMP
        max_temp_time = None
        for time in self.times_dict.keys():
            temp = self.get_time_object(time).get_temp()
            if temp >= max_temp:
                max_temp = temp
                max_temp_time = time

        return max_temp, max_temp_time

    def get_min_temp_and_time(self):
        min_temp = INIT_MIN_TEMP
        min_temp_time = None
        for time in self.times_dict.keys():
            temp = self.get_time_object(time).get_temp()
            if temp <= min_temp:
                min_temp = temp
                min_temp_time = time

        return min_temp, min_temp_time

    def get_rain_description_and_time_tuple_list(self):
        lst = []
        for time in self.times_dict.keys():
            weather_des = self.get_time_object(time).get_weather_description()
            if "rain" in weather_des:
                lst.append((weather_des, time))
        return lst


class Time:
    """ Class
    """
    def __init__(self, time_data_dict):
        self.time_data_dict = time_data_dict
        self.time = self.get_data_time()

    def get_time(self):
        return self.time

    def get_data_time(self):
        return self.time_data_dict.get(DATE_TIME_KEY)[11:]

    def get_temp(self):
        return self.time_data_dict.get(MAIN_TEMP_KEY).get(TEMP_KEY)

    def get_max_temp(self):
        return self.time_data_dict.get(MAIN_TEMP_KEY).get(MAX_TEMP_KEY)

    def get_min_temp(self):
        return self.time_data_dict.get(MAIN_TEMP_KEY).get(MIN_TEMP_KEY)

    def get_weather_description(self):
        return self.time_data_dict.get(WEATHER_KEY)[0].get(WEATHER_DESCRIPTION_KEY)

#get weather status
