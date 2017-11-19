from Reminders import Reminders

class User:

    def __init__(self, name, feats, email, city_data, rem_sheet_name, unit='imperial'):

        self.name = name
        self.email = email
        self.city_name = city_data[0]
        self.country_code = city_data[1]
        self.reminders = Reminders(rem_sheet_name)
        self.feats = feats
        self.unit = unit
