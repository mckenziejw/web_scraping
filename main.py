# Scrape some website dude

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from pprint import pprint
import pandas as pd
import numpy as np
 
url = 'https://lolesports.com/schedule?leagues=lec,european-masters,lcs' 
 
driver = webdriver.Chrome(service=ChromeService( 
    ChromeDriverManager().install())) 
 
driver.get(url) 
elements = driver.find_elements(By.CLASS_NAME, 'EventMatch') 
matches = []
for title in elements: 
    new_event = {'team1':'', 'team2':''}
    team1 = title.find_element(By.CLASS_NAME, 'team1')
    team1 = team1.find_element(By.CLASS_NAME, 'team-info')
    team1 = team1.find_element(By.TAG_NAME, 'h2').find_elements(By.TAG_NAME, 'span')[1].text
    new_event['team1'] = team1
    team2 = title.find_element(By.CLASS_NAME, 'team2')
    team2 = team2.find_element(By.CLASS_NAME, 'team-info')
    team2 = team2.find_element(By.TAG_NAME, 'h2').find_elements(By.TAG_NAME, 'span')[1].text
    new_event['team2'] = team2
    matches.append(new_event)
pd_matches = pd.DataFrame(matches)

def evaluate_arbitrage():
    return True

