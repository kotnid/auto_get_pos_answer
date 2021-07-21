from selenium import webdriver 
from time import sleep 
import logging
import webbrowser
import csv 

from .words import not_used

pos = {'verb','noun','adjective','adverb'}

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler('eng.log','w','utf-8')])

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

DRIVER_PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver'
driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)

words = not_used()

with open('answer.csv', 'w', encoding='utf-8')as f:
    writer = csv.writer(f)
    for i in words:
        list = [] 
        for u in pos:
            url = f"https://www.wordhippo.com/what-is/the-{u}-for/{i}.html"
            driver.get(url)
            try:
                h1 = driver.find_element_by_class_name('defv2wordtype').text
                list.append(f"{h1}({u})")
            except:
                list.append(f"N/A({u})")    
            sleep(1)


        logging.info(list)
        writer.writerow(list)

webbrowser.open('answer.csv')

