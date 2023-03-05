# Scrape some website dude

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import pandas as pd
import numpy as np
import time
from selenium.webdriver.chrome.options import Options
import re

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-site-isolation-trials")

# game_map_esportsbet = {
#     "lol": "League of Legends",
#     "kog" : "kog",
#     "csgo": "CSGO",
#     "wr": "Wild Rift",
#     ""
# }


def scroll(driver, timeout):
    scroll_pause_time = timeout
    # Get scroll height
    last_height = driver.execute_script(
        "return document.getElementsByTagName('iframe')[2].contentWindow.document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script(
            "document.getElementsByTagName('iframe')[2].contentWindow.scrollTo(0, document.getElementsByTagName('iframe')[2].contentWindow.document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.getElementsByTagName('iframe')[2].contentWindow.document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


url = 'https://esportsbet.io/esportsbull/'

driver = webdriver.Chrome(chrome_options=chrome_options, service=ChromeService(
    ChromeDriverManager().install()))

driver.get(url)
time.sleep(10)
driver.switch_to.frame(2)
# Find all match elements
elements = driver.find_element(
    By.CLASS_NAME, 'gamesListins_content')
match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
# pprint(match_div)
old_match_id = 0
match_id = 1
while old_match_id != match_id:
    old_match_id = match_div[-1].get_attribute('data-parentmatchid')
    match_div[-1].location_once_scrolled_into_view
    time.sleep(3)
    elements = driver.find_element(
        By.CLASS_NAME, 'gamesListins_content')
    match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
    match_id = match_div[-1].get_attribute('data-parentmatchid')

elements = driver.find_element(
    By.CLASS_NAME, 'gamesListins_content')
matches = elements.find_elements(By.CSS_SELECTOR, 'div a')
# Time to extract the useful data
match_list = []
for match in matches:
    new_line = {'esportsbet_id': '', 'date': '', 'time': '',
                'home_team': '', 'away_team': '', 'home_odds': '', 'away_odds': '', 'link': ''}
    new_line['esportsbet_id'] = match.get_attribute('data-parentmatchid')

    new_line['date'] = re.sub("<span.*", '', match.find_element(
        By.CSS_SELECTOR, 'div.date').get_attribute('innerHTML'))
    new_line['time'] = re.sub("<span.*", '', match.find_element(
        By.CSS_SELECTOR, 'div.time').get_attribute('innerHTML'))
    new_line['home_team'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamHome').find_element(By.CSS_SELECTOR, 'div.team_title').text
    new_line['home_odds'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamHome').find_element(By.CSS_SELECTOR, 'div.odds').text
    new_line['away_team'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamAway').find_element(By.CSS_SELECTOR, 'div.team_title').text
    new_line['away_odds'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamAway').find_element(By.CSS_SELECTOR, 'div.odds').text
    new_line['link'] = match.get_attribute('href')
    match_list.append(new_line)
pd_esportsbet_matches = pd.DataFrame(match_list)

## Repeat it for gg.bet

url = 'https://esportsbet.io/esportsbull/'

driver = webdriver.Chrome(chrome_options=chrome_options, service=ChromeService(
    ChromeDriverManager().install()))

driver.get(url)
time.sleep(10)
driver.switch_to.frame(2)
# Find all match elements
elements = driver.find_element(
    By.CLASS_NAME, 'gamesListins_content')
match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
# pprint(match_div)
old_match_id = 0
match_id = 1
while old_match_id != match_id:
    old_match_id = match_div[-1].get_attribute('data-parentmatchid')
    match_div[-1].location_once_scrolled_into_view
    time.sleep(3)
    elements = driver.find_element(
        By.CLASS_NAME, 'gamesListins_content')
    match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
    match_id = match_div[-1].get_attribute('data-parentmatchid')

elements = driver.find_element(
    By.CLASS_NAME, 'gamesListins_content')
matches = elements.find_elements(By.CSS_SELECTOR, 'div a')
# Time to extract the useful data
match_list = []
for match in matches:
    new_line = {'esportsbet_id': '', 'date': '', 'time': '',
                'home_team': '', 'away_team': '', 'home_odds': '', 'away_odds': '', 'link': ''}
    new_line['esportsbet_id'] = match.get_attribute('data-parentmatchid')

    new_line['date'] = re.sub("<span.*", '', match.find_element(
        By.CSS_SELECTOR, 'div.date').get_attribute('innerHTML'))
    new_line['time'] = re.sub("<span.*", '', match.find_element(
        By.CSS_SELECTOR, 'div.time').get_attribute('innerHTML'))
    new_line['home_team'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamHome').find_element(By.CSS_SELECTOR, 'div.team_title').text
    new_line['home_odds'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamHome').find_element(By.CSS_SELECTOR, 'div.odds').text
    new_line['away_team'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamAway').find_element(By.CSS_SELECTOR, 'div.team_title').text
    new_line['away_odds'] = match.find_element(
        By.CSS_SELECTOR, 'div.teamAway').find_element(By.CSS_SELECTOR, 'div.odds').text
    new_line['link'] = match.get_attribute('href')
    match_list.append(new_line)
pd_esportsbet_matches = pd.DataFrame(match_list)

