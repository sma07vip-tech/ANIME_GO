from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup
from datetime import date


class Anime:
    service = Service(executable_path=ChromeDriverManager().install())
    
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=self.service) 
        self.driver.get(self.url)
        time.sleep(3)
        
    #TYPE
    def serial(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Сериал']").click()
        time.sleep(3)
    
    def film(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Фильм']").click()
        time.sleep(3)
    
    def OVA(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'OVA']").click()
        time.sleep(3)
    
    def speshl(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Спешл']").click()
        time.sleep(3)
    
    def ONA(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'ONA']").click()
        time.sleep(3)
    
    #STATUS
    def ongoing(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Онгоинг']").click()
        time.sleep(3)
    
    def came_out(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Вышел']").click()
        time.sleep(3)
    
    def anons(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Анонс']").click()
        time.sleep(3)
    
    def recently(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Недавно']").click()
        time.sleep(3)
    
    #AGE
    def G(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'G']").click()
        time.sleep(3)
    
    def PG(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'PG']").click()
        time.sleep(3)
    
    def PG_13(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'PG-13']").click()
        time.sleep(3)
    
    def R_17(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'R-17']").click()
        time.sleep(3)
    
    def R(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'R+']").click()
        time.sleep(3)
    
    #Number_of_episodes
    def long(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Длинные']").click()
        time.sleep(3)
    
    def short(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Короткие']").click()
        time.sleep(3)
    
    def mid(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Средние']").click()
        time.sleep(3)
    
    def long_long(self):
        self.driver.find_element("xpath", "//label[normalize-space() = 'Очень длинные']").click()
        time.sleep(3)
    
    #FILTER_AGE
    def filter_1(self, year_1):
        try:
            year_1_int = int(year_1)
            if year_1_int < 1959:
                raise AssertionError("Год должен быть не меньше 1959")
            self.driver.find_element("xpath", "//input[@name = 'year_from']").send_keys(str(year_1_int))
            time.sleep(3)
        except ValueError:
            raise AssertionError("Ошибка: нужно ввести число")

    def filter_2(self, year_2):
        try:
            year_2_int = int(year_2)
            if int(date.today().year)<year_2_int:
                raise AssertionError("ошибка ввода года должен быть меньше текущего")
            self.driver.find_element("xpath", "//input[@name = 'year_to']").send_keys(str(year_2_int))
            time.sleep(3)
        except ValueError:
            raise AssertionError("Ошибка: нужно ввести число")

    def all_div(self):
        lst =[]
        all=self.driver.find_elements("xpath","//div[@class='ani-list__item-title h5 fw-normal mb-1 d-inline-grid']")
        
        for item in all:
            print(item.text)
        
        
        

