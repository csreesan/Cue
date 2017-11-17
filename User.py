from Reminders import Reminders


class User:

	def __init__(self, name, feats, email, cityData, remindersSheetName, unit='imperial'):

		self.name = name
		self.email = email
		self.cityName = cityData[0]
		self.countryCode = cityData[1]
		self.reminders = Reminders(self.name, remindersSheetName)
		self.feats = feats
		self.unit = unit
