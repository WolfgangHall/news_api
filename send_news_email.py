import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys
sys.path.insert(0, r'D:\app') # grants access to Account Details
from news_account_info import AccountDetails


class SendEmail:

    my_email = AccountDetails.email
    password = AccountDetails.email_password

    def __init__(self, subject, body):
        self._msg = MIMEMultipart()
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._subject = subject
        self._body = body

        self.generate_msg(self._subject, self._body)
        self.create_server()

    def generate_msg(self, subject, body):
        '''Adds From email, To email, Subject heading and adds the message body'''
        self._msg['From'] = SendEmail.my_email
        self._msg['To'] = SendEmail.my_email
        self._msg['Subject'] = 'News for {}'.format(subject)
        self._msg.attach(MIMEText(body, 'html'))

    def create_server(self):
        '''Starts email server and sends email'''
        self._server.starttls()
        self._server.login(SendEmail.my_email, SendEmail.password)
        text = self._msg.as_string()
        self._server.sendmail(SendEmail.my_email, SendEmail.my_email, text)
        self._server.quit()
