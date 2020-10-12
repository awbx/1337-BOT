
from selenium import webdriver
import pyttsx3
import time
import json
import re


engine = pyttsx3.init()

config = json.load(open('config.json'))

keyword_used = [
    'Date de la rentrée',
    'Nombre de places',
    'places libres',
    'S\'inscrire',
    'Plus de place',
    'Accompagnement',
    'Ben Guerir',
    'Khouribga',
    'Je viens avec quelqu\'un',
    '25000',
    '43150'
    ]

URL = config["URL_TEST"] if config['testing'] else config['URL']

chrome = webdriver.Chrome('./chromedriver')

chrome.get(URL)


def notify():
    try:
        for i in range(200):
            engine.say("Worning Something There")
            engine.runAndWait()
    except:
        engine.stop()
def login():
    if '/users/sign_in' in chrome.current_url:
        pass
    elif '/users/sign_in' not in chrome.current_url:
        return True
    else:
        chorme.get(URL+'users/sign_in')
    chrome.implicitly_wait(1)
    email = chrome.find_element_by_name(config['emailName'])
    password = chrome.find_element_by_name(config['passName'])
    commit = chrome.find_element_by_name('commit')
    
    if email and password and commit:
        email.send_keys(config['email'])
        password.send_keys(config['password'])
        commit.submit()
        return True
        
def check_pool():
    if 'piscines' in chrome.current_url:
        pass
    else:
        chrome.get(URL+"piscines")
    chrome.implicitly_wait(1)
    is_found = list(filter(lambda x: re.search(x,chrome.page_source),keyword_used))
    if len(is_found) > 0:
        notify()

def check_check_in():
    if 'meetings' in chrome.current_url:
        pass
    else:
        chrome.get(URL + 'meetings')
    chrome.implicitly_wait(1)
    is_found = list(filter(lambda x: re.search(x,chrome.page_source),keyword_used))
    if len(is_found) > 0:
        notify()
def refresh():
    chrome.refresh()
def sleep(sec):
    time.sleep(sec)
def check_testing_type():
    if config['testing_type'] == '0':
        check_check_in()
    elif config['testing_type'] == '1':
        check_pool()
    else: # elif config['testing_type'] == '2' => Same
        check_check_in()
        check_pool()


try:
    while True:
        refresh()
        if config['testing']:
            check_testing_type()
        else:
            if login():
                check_testing_type()
            else:
                login()
        sleep(8)

except KeyboardInterrupt:
    chrome.quit()
except Exception as e :
    print(e)
finally:
    print("\nBye :-)")



    
