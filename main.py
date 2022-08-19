# import module
from urllib.request import urlopen
from urllib.error import *
import time
import logging

def healthchecks(url):
    while True:
        # try block to read URL

        try:
            html = urlopen(url)

        except HTTPError as e:
            logging.critical('HTTP error')

        except URLError as e:
            print("Opps ! Page not found!", e)
            logging.critical('Opps ! Page not found!')
        else:
            print('OK')
            logging.warning('OK')
        time.sleep(2.5)


healthchecks("http://54.226.113.122:56733/template")

