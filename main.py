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
import class_file as cf


print("Парсер Anime GO")

anime = cf.Anime("https://animego.me/anime")


proverka = input("Вы хотите выбрать тип аниме (да/нет)")
if proverka.lower() == 'нет':pass
elif proverka.lower() == 'да':
    type_anime = input("Anime какого типа ты хочешь (Сериал,Фильм,OVA,ONA,Спешл)")
    
    if type_anime.lower() == 'сериал':anime.serial()
    elif type_anime.lower() == 'фильм':anime.film()
    elif type_anime.lower() == 'ova':anime.OVA()
    elif type_anime.lower() == 'ona':anime.ONA()
    elif type_anime.lower() == 'спешл':anime.speshl()
    else:
        print("При парсинге тип аниме будет отсутствовать ошибка ввода аниме")
else:pass


proverka = input("Вы хотите выбрать статус аниме (да/нет)")
if proverka.lower() == 'нет':pass
elif proverka.lower() == 'да':
    type_anime = input("Anime какого статуса ты хочешь (Онгоинг,Вышел,Анонс,Недавно)")
    
    if type_anime.lower() == 'онгоинг':anime.ongoing()
    elif type_anime.lower() == 'вышел':anime.came_out()
    elif type_anime.lower() == 'анонс':anime.anons()
    elif type_anime.lower() == 'недавно':anime.recently()
    else:
        print("При парсинге статус аниме будет отсутствовать ошибка ввода статуса")
else:pass


proverka = input("Вы хотите выбрать возрастное ораничение аниме (да/нет)")
if proverka.lower() == 'нет':pass
elif proverka.lower() == 'да':
    type_anime = input("Anime какого возрастного ограничения ты хочешь (G,PG,PG-13,R-17,R+)")
    
    if type_anime.lower() == 'g':anime.G()
    elif type_anime.lower() == 'pg':anime.PG()
    elif type_anime.lower() == 'pg-13':anime.PG_13()
    elif type_anime.lower() == 'r-17':anime.R_17()
    elif type_anime.lower() == 'r+':anime.R()
    else:
        print("При парсинге возрастное ограничение аниме будет отсутствовать ошибка ввода возрастного ограничения")
else:pass


proverka = input("Вы хотите выбрать количество серий аниме (да/нет)")
if proverka.lower() == 'нет':pass
elif proverka.lower() == 'да':
    type_anime = input("Anime какого количества серий ты хочешь (Короткие,Средние,Длинные,Очень длинные)")
    
    if type_anime.lower() == 'короткие':anime.short()
    elif type_anime.lower() == 'средние':anime.mid()
    elif type_anime.lower() == 'длинные':anime.long()
    elif type_anime.lower() == 'очень длинные':anime.long_long()
    else:
        print("При парсинге возрастное количество серий аниме будет отсутствовать ошибка ввода количества серий аниме")
else:pass

proverka = input("Вы хотите выбрать фильтрацию по года (да/нет)")
if proverka.lower() == 'нет':pass
elif proverka.lower() == 'да':
    type_anime = input("выбор(от и до,только от и до текущего, от 1959 до нашего года)")
    
    if type_anime.lower() == 'от и до':
        try:
            anime.filter_1(input("введи год от которого -> "))
            anime.filter_2(input("введи год до которого -> "))
        except AssertionError as e :
            print(e)
            print("при парсинге годы учитываться не будут из-за ошибки ввода")
    elif type_anime.lower() == 'только от и до текущего':
        try:
            anime.filter_1(input("введи год от которого -> "))
        except AssertionError as e:
            print(e)
            print("при парсинге годы учитываться не будут из-за ошибки ввода")
    elif type_anime.lower() == 'от 1959 до нашего года':
        try:
            anime.filter_2(input("введи год до которого -> "))
        except AssertionError as e:
            print(e)
            print("при парсинге годы учитываться не будут из-за ошибки ввода")
    else:
        print("годы не учитываются т.к. ошибка ввода")
else:pass

anime.all_div()