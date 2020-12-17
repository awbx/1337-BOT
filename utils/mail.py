from email.message import EmailMessage
import smtplib
import json
import ssl
import os

config = json.load(
    open(os.path.join(os.path.dirname(__file__), '../config.json')))

HOST = config.get('SMTP_HOST', None)
PORT = int(config.get('SMTP_PORT', 587))
USER = config.get('SMTP_USER', None)
PASS = config.get('SMTP_PASS', None)
SENDER = config.get('SMTP_SENDER', None)
RECEIVER = config.get('SMTP_RECEIVER', None)
USE_TLS = True

context = ssl.create_default_context()


class Mailer(smtplib.SMTP):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.start_connection()
        self.start_login()

    def start_connection(self):
        """ This Function Will Start Connection Between SMTP Client & Server """
        try:
            super().__init__(host=self.host, port=self.port)
            self.ehlo()
            if USE_TLS:
                self.starttls(context=context)
                self.ehlo()
        except Exception as e:
            print(f"Error : {e}")

    def start_login(self):
        """ This Funcntion Will Handle The Authentication Process """
        try:
            self.ehlo()
            self.login(USER, PASS)
        except smtplib.SMTPAuthenticationError:
            print("username/password incorrect !")
        except smtplib.SMTPNotSupportedError:
            print("Please use TLS !")
        except Exception as e:
            print(f"Error : {e}")

    def send_mail(self, body, to=RECEIVER, from_=SENDER, subject="1337 Bot"):
        """ This Function Will Send An Email """
        try:
            self.ehlo()
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = from_
            msg['To'] = to
            msg.set_content(body)
            self.send_message(msg)
        except Exception as e:
            print(f"Error: {e}")

    def __del__(self):
        """ Close Connection """
        self.close()
