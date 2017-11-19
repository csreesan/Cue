# -*- coding: utf-8 -*-
import smtplib
#from HtmlString import HtmlString
from WeatherMessage import WeatherMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from User import User
import datetime
import email.mime.application

CONTACT_DICT = dict(Jason='cue.me.today@gmail.com')
from email.mime.image import MIMEImage

class cue:
    """ Actual cuer and takes in a list
        of desired items in email. Sends
        the email, formatted.
    """
    day_of_week = {0 : 'Monday',
                   1 : 'Tuesday',
                   2 : 'Wednesday',
                   3 : 'Thursday',
                   4 : 'Friday',
                   5 : 'Saturday',
                   6 : 'Sunday'}

    months = {1 : 'January',
              2 : "February",
              3 : "March",
              4 : "April",
              5 : "May",
              6 : "June",
              7 : "July",
              8 : "August",
              9 : "September",
              10 : "October",
              11 : "November",
              12 : "December"}

    def __init__(self, user):
        self.mailer = smtplib.SMTP('smtp.gmail.com', 587)
        self.mailer.ehlo()
        self.mailer.starttls()
        self.mailer.login('cue.me.today@gmail.com', 'okay12345')

        self.user = user
        self.name = self.user.name
        self.subject = "Your upcoming day, %s!" % self.user.name
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = "Your upcoming day, %s!" % self.user.name
        self.msg['From'] = self.msg['To'] = user.email
        self.weather_message = WeatherMessage(user.city_name, user.country_code, user.unit)

        # self.msg = "Dear %s," % name
        self.feats = user.feats

        self.composer()

    def composer(self):
        """ Creates the string used
            to send the email and
            creates html page if possible.
        """
        added = []
        for feat in self.feats:
            if feat == 'task':
                added.append(self.user.reminders.compose())
            #add more features!

        text = self.alt(added)
        #html = HtmlString(self.name, added).compose()

        part1 = MIMEText(text, 'plain')
        #part2 = MIMEText(html, 'html')
        self.msg.attach(part1)

        for file in self.user.reminders.get_attachments():
            self.msg.attach(file)

        #self.msg.attach(part2)
        #self.msg.attach(msgImage)


    def alt(self, added):
        """ alternative email in case
            html fails to send.
        """
        wd = datetime.datetime.today().weekday()
        month = datetime.date.today().month
        day = datetime.date.today().day

        msg = "Good Morning, %s" \
              "\nToday is %s, %s %s." \
              % (self.name, self.day_of_week[wd], self.months[month], day)
        msg = msg + "\n" + self.weather_message.compose()

        for add in added:
            msg = msg + "\n" + add

        return msg


    def mail(self):
        """ Sends the daily email notifiation
            with wanted features.
        """
        """
        self.mailer.sendmail('cue.me.today@gmail.com',
                             self.contact[self.name],
                             'Subject: %s<br>%s' % (self.subject, self.msg))        
        """
        print('sent')
        self.mailer.sendmail('cue.me.today@gmail.com',
                             self.user.email,
                             self.msg.as_string())


def main():
    """ Read the correct profile.
    """
    jason = User('Jason', ['task'], 'cue.me.today@gmail.com', ['Berkeley', 'us'], 'jason')
    q = cue(jason)
    q.mail();

if __name__=='__main__':
  main()
