from .models import CustomerHBD
import smtplib
import datetime


# datetime object containing current date and time
now = datetime.datetime.now()
today=now.strftime("%Y-%m-%d")



to = 'saikrishnavadali05@gmail.com'
to2 = 'raviteja.sssihl@gmail.com'
GMAIL_ID = 'multiplewishes.py@gmail.com'
GMAIL_PSWD = 'swamigrace'


def sending_mail_job():   
    #username = CustomerHBD.objects.filter(date = today)
    #date_today_db=str(username)
    #print(date_today_db[25:35])
    #if str(date_today_db) == str(today): 
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(GMAIL_ID, GMAIL_PSWD)
        s.sendmail(GMAIL_ID, to, f"First testing wish")
        s.sendmail(GMAIL_ID, to2, f"first wish")
        s.quit()