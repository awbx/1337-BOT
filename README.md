# 1337 Bot

This's a bot script to check if CHECK-IN or POOL exist and it will notify if exist using sound , mail or call !

## Features:

---

- Login With Your Credentials
- Check If Check-In Or Pool Exist
- Notify Using Sound
- Repeat Checking Every N Seconds As You Want
- Notify Using Mail with SMTP
- ~~Notify Using Call with Twilio API <sup>SOON</sup>~~

### Installation & Running:

---

```diff
- Note: Before all that you must have python3 on your OS
```

> In Case You Want To Install And Run This Bot You Should Follow This Steps Below . :point_down:

1. Get The Requirements:

   - `pip3 install -r requirements.txt`

2. Download WebDriver For Google Chrome:

   - **NOTE : In Case You Use Google Chrome 86.0.4240.75 That's Work For You Don't Need Download Anything.**
   - Go to this [link](https://chromedriver.chromium.org/downloads) and download ChromeDriver as per your Google Chrome version ! After that unzip it in the Bot folder.

3. Set Credentials:
   - Use any IDE and open `config.json` and change the following to your credentials.
   ```
   {
   "SMTP_HOST": "YOUR SMTP HOST",
   "SMTP_PORT": "YOUR SMTP PORT",
   "SMTP_USER": "YOUR SMTP USER",
   "SMTP_PASS": "YOUR SMTP PASS",
   "SMTP_SENDER": "YOUR SMTP SENDER",
   "SMTP_RECEIVER": "YOUR SMTP RECEIVER",
   "EMAIL": "YOUR 1337 EMAIL",
   "PASSWORD": "YOUR 1337 PASSWORD",
   }
   ```
4. Run The Bot:
   - `python3 run.py`

### Tech

1337 Bot built with this libraries and frameworks :

- [Selenium](https://www.selenium.dev/) - Selenium is a portable framework for testing web applications.
- [Pyttsx3](https://pypi.org/project/pyttsx3/) - text-to-speech conversion library in Python.
- [smtplib](https://docs.python.org/3/library/smtplib.html) - smtplib is Python's built-in module for sending emails to any Internet machine with an SMTP or ESMTP listener daemon. 
### Follow Us !

- [Facebook](https://www.facebook.com/abdlehadi.sabani)
- [Twitter](https://twitter.com/AbdelhadiSabani)
- [LinkedIn](https://www.linkedin.com/in/abdelhadi-sabani-1bb5171a7/)
- [GitHub](https://github.com/awbx)

### License

---

MIT &copy; [Awbx](https://github.com/awbx)

**Free Software, Hell Yeah!**
