import imaplib
import email

mail = imaplib.IMAP4_SSL('outlook.office365.com')
creds = open('../emailcreds.txt','r')
print creds
