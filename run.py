from selenium.webdriver import Chrome
from os import path
import pyttsx3
import json
import time
import re


config = json.load(open("config.json"))
URL = config['URL']

KEYWORD_USED = config.get('KEYWORD_USED', None)
ASSAY_TYEPS_AVAILABLE = config.get("ASSAY_TYPES_AVAILABLE", None)
ASSAY_TYPE = config.get("ASSAY_TYPE", "BOTH")
REPEAT_AFTRE_N_SEC = config.get("REPEAT_AFTRE_N_SEC", 6)


class Bot(Chrome):
    def __init__(self, webdriver_name="./chromedriver"):
        self.webdriver_name = webdriver_name

    def start_chrome(self):
        """ This Function Will Start Google Chrome Driver """
        super().__init__(self.webdriver_name)
        self.get(URL)
        self.implicitly_wait(1)
        self.engine = pyttsx3.init()

    def notify(self):
        try:
            for _ in range(200):
                self.engine.say("Warning Something There")
                self.engine.runAndWait()
        except:
            self.engine.stop()

    def login(self):
        """ This Function Will Login To 1337 With Your Credentials """
        if '/users/sign_in' in self.current_url:
            pass
        elif '/users/sign_in' not in self.current_url:
            return True
        else:
            self.get(path.join(URL, 'users/sign_in'))
        self.implicitly_wait(1)
        email = self.find_element_by_name("user[email]")
        password = self.find_element_by_name("user[password]")
        commit = self.find_element_by_name('commit')

        if email and password and commit:
            email.send_keys(config.get("EMAIL", None))
            password.send_keys(config.get('PASSWORD', None))
            commit.submit()
            return True

    def check_pool(self):
        if 'piscines' in self.current_url:
            pass
        else:
            self.get(path.join(URL, "piscines"))
        self.implicitly_wait(1)
        is_found = self.exist_in_page_source()
        if len(is_found) > 0:
            self.notify()

    def check_check_in(self):
        if 'meetings' in self.current_url:
            pass
        else:
            self.get(path.join(URL, 'meetings'))
        self.implicitly_wait(1)
        is_found = self.exist_in_page_source()
        if len(is_found) > 0:
            self.notify()

    def assay_type(self):
        if ASSAY_TYEPS_AVAILABLE.get(ASSAY_TYPE, None) == 0:
            self.check_check_in()
        elif ASSAY_TYEPS_AVAILABLE.get(ASSAY_TYPE, None) == 1:
            self.check_pool()
        elif ASSAY_TYEPS_AVAILABLE.get(ASSAY_TYPE, None) == 2:
            self.check_check_in()
            self.check_pool()
        else:
            raise KeyError("Assay Type Not Found")

    def exist_in_page_source(self):
        return list(filter(lambda x: re.search(x, self.page_source), KEYWORD_USED))

    def repeat_after_n_sec(self, sec=REPEAT_AFTRE_N_SEC):
        time.sleep(sec)


bot = Bot()
bot.start_chrome()
bot.login()

while True:
    try:
        bot.refresh()
        if bot.login():
            bot.assay_type()
        else:
            bot.login()
        bot.repeat_after_n_sec()
    except KeyboardInterrupt:
        bot.quit()
        print("\rGoodBye :)")
        exit(0)
    except Exception as e:
        print(e)
        bot.quit()
        break
