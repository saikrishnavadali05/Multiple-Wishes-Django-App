from .models import CustomerHBD
import smtplib
import datetime
from googletrans import Translator


# datetime object containing current date and time
now = datetime.datetime.now()
today=now.strftime("%Y-%m-%d")



to = 'saikrishnavadali05@gmail.com'
to2 = 'raviteja.sssihl@gmail.com'
#mother = 'sarada24v@gmail.com'
#father = 'sathyanarayanavadali1969@gmail.com'
GMAIL_ID = 'multiplewishes.py@gmail.com'
GMAIL_PSWD = 'swamigrace'
sub = "Multiple Wishes on your wedding anniversary from multiple Wishes"
msg = "Wish you a very happy Wedding anniversary!!!"

def sending_mail_job():   
        translator=Translator()
        #msg = translator.translate(msg,dest='fr')
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(GMAIL_ID, GMAIL_PSWD)

        s.sendmail(GMAIL_ID, to2, f"Subject : {sub}\n\n{msg}")
        #s.sendmail(GMAIL_ID, to, f"Subject : {sub}\n\n{msg}")
        
        #s.sendmail(GMAIL_ID, mother, f"Subject : {sub}\n\n{msg}")
        #s.sendmail(GMAIL_ID, father, f"Subject : {sub}\n\n{msg}")
        s.quit()

###Working code for iterate to DB
#userdata = CustomerHBD.objects.all()
#        for i in userdata:
#            msg = i.name
###