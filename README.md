# 1337 Bot

This's a bot script to check if CHECK-IN or POOL exist and it will notify if exist using sound !

## Features:
----

-  Login With Your Credentials
- Check If Check-In Or Pool Exist
-  Notify Using Sound
-  Repeat Checking Every N Seconds As You Want
-  ~~Notify Using Call with Twilio API <sup>SOON</sup>~~
-  ~~Notify Using Mail with SMTP <sup>SOON</sup>~~ 

### Installation & Running:
----

```diff
- Note: Before all that you must have python3 on your OS
```

> In Case You Want To Install And Run This Bot You Should Follow This Steps Below . :point_down: 

1. Get The Requirements:
    * ```pip3 install -r requirements.txt```

2. Download WebDriver For Google Chrome:

      **NOTE : In Case You  Use Google Chrome 86.0.4240.75 That's Work For You Don't Need Download Anything.**
      Go to this [link](https://chromedriver.chromium.org/downloads) and download ChromeDriver as per your Google Chrome version ! After that unzip it in the Bot folder.
3. Set Credentials:
      Use any IDE and open ```config.json``` and change email and password to your credentials<br/>
      ```
      {
    "email":"YOUR 1337 EMAIL",
    "password":"YOUR PASSWORD",
      }
      ```
4. Run The Bot:
      ```python3 bot.py```
### License
----

MIT


**Free Software, Hell Yeah!**
