from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime

class HtmlString:
    wd = datetime.datetime.today().weekday()
    month = datetime.date.month
    day = datetime.date.day

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
        """

    def __init__(self, name, added):
        self.added = added

    def compose(self):



    """html code as string format"""

html = 'hello <img src="cid:image1">'
        fp = open('1.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')

     % (self.weather_message.compose(), self.user.reminders.compose())
        print(html)