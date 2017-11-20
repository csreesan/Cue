from email.mime.image import MIMEImage
import datetime

class HtmlString:
    wd = datetime.datetime.today().weekday()
    month = datetime.date.month
    day = datetime.date.day

    html = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Yantramanav:400,900" rel="stylesheet">   
  </head>
  <body style="margin: 0; padding: 0;">
    <table align="center" style="border-spacing:10px;border-collapse:separate;text-align:left;width:600px;margin:auto;">
      <tr>
        <td style="padding:10px;">
          <i>cue: your daily digest</i>
          <h1 style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">Good Morning, %s.</h1>
          <p style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">%s.<br>
             Here's some things to get you ready for the day.</p>
          <hr style="border-color:black;">
        </td>
      </tr>
      <tr>
        <td bgcolor="#ffffff" style="padding:10px;">
          <h2 style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">Weather</h2>
          <img src="cid:image1" style="width:auto;max-width:150px;height:auto;max-height:100px;">
          <p style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">%s</p>
        </td>
      </tr>
      <tr>
        <td bgcolor="#ffffff" style="padding:10px;">
          <h2 style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">Tasks</h2>
          <p style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">%s</p>
        </td>
      </tr>
      <tr>
        <td bgcolor="#ffffff" style="padding:10px;">
          <h2 style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">Reminders</h2>
          <p style="padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;">Remember to ...</p>
        </td>
      </tr>
      <tr>
        <td bgcolor="#2ecc71" style="padding:10px;">
          <p1 style="display:block;padding:0px;margin:0px;font-family:'Yantramanav', sans-serif;color:white;text-align:center;"><center>That's all. Enjoy your day!</center></p1>
        </td>
      </tr>
    </table>
  </body>
</html>
            """

    def __init__(self, name, added, date, w):
        self.name = name
        self.date = date
        self.added = added
        self.w = w


    def composeText(self):
        msg = self.html % (self.name, self.date, self.w ,self.added[0])
        return msg

    def composeImage(self):
        fp = open('1.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        return msgImage

