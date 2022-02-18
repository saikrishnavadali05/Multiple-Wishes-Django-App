from .models import CustomerHBD
import smtplib

to = 'saikrishnavadali05@gmail.com'
GMAIL_ID = 'pseudotesting5@gmail.com'
GMAIL_PSWD = 'omsrisairam'


def sending_mail_job():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"If you receive this mail it means the server is up and running without any manual intervention sending mail every minute")
    s.quit()