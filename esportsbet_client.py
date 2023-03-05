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


class esportsbetClient:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--disable-site-isolation-trials")

        self.url = 'https://esportsbet.io/esportsbull/'

    def fetch(self):
        self.driver = webdriver.Chrome(
            chrome_options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.url)
        time.sleep(10)
        self.driver.switch_to.frame(2)
# Find all match elements
        elements = self.driver.find_element(
            By.CLASS_NAME, 'gamesListins_content')
        match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
        # pprint(match_div)
        old_match_id = 0
        match_id = 1
        end_found = False
        # Do the silly scroll logic
        while not end_found:
            old_match_id = match_div[-1].get_attribute('data-parentmatchid')
            match_div[-1].location_once_scrolled_into_view
            time.sleep(3)
            elements = self.driver.find_element(
                By.CLASS_NAME, 'gamesListins_content')
            match_div = elements.find_elements(By.CSS_SELECTOR, 'div a')
            match_id = match_div[-1].get_attribute('data-parentmatchid')
            match_count = self.driver.find_element(
                By.CSS_SELECTOR, 'div.match_count').text
            if len(match_div) >= int(match_count):
                end_found = True

        elements = self.driver.find_element(
            By.CLASS_NAME, 'gamesListins_content')
        matches = elements.find_elements(By.CSS_SELECTOR, 'div a')
        # Get match count value

        # Time to extract the useful data
        match_list = []
        for match in matches:
            new_line = {'esportsbet_id': '', 'date': '', 'time': '',
                        'home_team': '', 'away_team': '', 'home_odds': '', 'away_odds': '', 'link': ''}
            new_line['esportsbet_id'] = match.get_attribute(
                'data-parentmatchid')

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
        return pd_esportsbet_matches


fetch_boy = esportsbetClient()
results = fetch_boy.fetch()
print(results.shape)
