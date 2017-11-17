import smtplib
from WeatherMessage import WeatherMessage
from Reminders import Reminders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from User import User

CONTACT_DICT = dict(Jason='cue.me.today@gmail.com')

class cue:
    """ Actual cuer and takes in a list
        of desired items in email/
    """

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
        self.weatherMessage = WeatherMessage(user.cityName, user.countryCode, user.unit)

        # self.msg = "Dear %s," % name
        self.feats = user.feats

        self.composer()

    def composer(self):
        """ Creates the string used
            to send the email.
        """

        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

        html = """\
        <html>
          <head>
          <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">
          </head>
          <style>

          h1 {
            font-family: 'Source Sans Pro', sans-serif;
          }

          p {
            font-family: 'Source Sans Pro', sans-serif;
          }


          </style>
            <body style="margin: 0; padding: 0;">
                <table align="center" border="1" bordercolor=BLACK cellpadding="50" cellspacing="0" width="600">
                 <tr>
                  <td bgcolor="#70bbd9">
                   <h1>Good Morning, Jason!</h1>
                   <p>Thursday, November 16, 2017.<br> Here's what's coming up today.</p>
                  </td>
                 </tr>
                 <tr>
                   <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
                    <table border="1" cellpadding="0" cellspacing="0" width="100%%">
                     <tr>
                      <td>
                       %s
                      </td>
                     </tr>
                     <tr>
                      <td>
                       %s
                       <iframe src="https://calendar.google.com/calendar/embed?src=cue.me.today%%40gmail.com&ctz=America%%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>             </tr>
                      </td>
                     </tr>
                     <tr>
                      <td>
                        <table border="1" cellpadding="0" cellspacing="0" width="100%%">
                         <tr>
                          <td width="50%%" valign="top">
                           some sort of interaction
                          </td>
                          <td style="font-size: 0; line-height: 0;" width="0%%">
                           &nbsp;
                          </td>
                          <td width="260" valign="top">
                            some sort of interaction2
                          </td>
                         </tr>
                        </table>
                      </td>
                     </tr>
                    </table>
                   </td>
                 </tr>
                 <tr>
                  <td bgcolor="#ee4c50">
                   <p>Have a good day and remember to bring your umbrella!</p>
                  </td>
                 </tr>
                </table>
            </body>
        </html>
        """ % (self.weatherMessage.compose(), self.user.reminders.compose())
        print(html)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        self.msg.attach(part1)
        self.msg.attach(part2)

        """
        if 'weather' in self.feats :
            self.msg += weather(self.name).compose()
        if 'task' in self.feats:
            self.msg += task(self.name).compose()
        """

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
                             CONTACT_DICT[self.name],
                             self.msg.as_string())



def main():
    """ Read the correct profile.
    """
    jason = User('Jason', ['task'], 'cue.me.today@gmail.com', ['Berkeley', 'us'], 'jason')
    q = cue(jason)
    q.mail();

if __name__=='__main__':
  main()
