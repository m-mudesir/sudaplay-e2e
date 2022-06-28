from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""
Testin screen script for SudaPlay for Sudani.
@author phantom-sage
"""

def test_home_page(): #1
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get('http://sudaplay.com/home')

   title = "SudaPlay Games - Online Games"
   assert title == chrome_driver.title

   chrome_driver.quit()


def test_category_action_page(): #2
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get('http://sudaplay.com/category/action/')


   
   assert "أكشن Games - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/category/action/"

   chrome_driver.quit()


def tests_puzzles_page(): #3
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/category/puzzles/")


   
   assert "الألغاز Games - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/category/puzzles/"

   chrome_driver.quit()


def test_strategy_page(): #4
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/category/strategy/")


   
   assert "الإستراتيجية Games - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/category/strategy/"

   chrome_driver.quit()

def test_traditional_page(): #5
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/category/traditional/")


   
   assert "التقليدية Games - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/category/traditional/"

   chrome_driver.quit()

def test_adventures_page(): #6
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/category/adventures/")


   
   assert "المغامرات Games - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/category/adventures/"

   chrome_driver.quit()

def test_subscribe_page(): #7
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/login/subscribe/")


   # Subscribe title have no title
   assert chrome_driver.current_url == "http://sudaplay.com/login/subscribe/"

   chrome_driver.quit()



def test_login_page(): #8
   options = webdriver.ChromeOptions()
   options.add_argument('headless')

   chrome_driver = webdriver.Chrome(chrome_options=options)
   chrome_driver.maximize_window()
   chrome_driver.get("http://sudaplay.com/login/login/")


   assert "Login - SudaPlay Games" == chrome_driver.title
   assert chrome_driver.current_url == "http://sudaplay.com/login/login/"

   chrome_driver.quit()