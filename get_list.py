from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv


driver = webdriver.Chrome("chromedriver")
# driver.get("http://google.com/search?q=selena+gomez")
# driver.get("https://google.com/search?q=Best+Hollywood+Celebrities")
# count = 0

file = open("list.txt", "r")
lines = file.readlines()
for line in lines:
	driver.get(f"http://google.com/search?q={line}")
	name = driver.find_element_by_css_selector("input[name='q']").get_attribute("value")
	print(name)
	# Getting Data
	# global count
	# count += 1
	time.sleep(random.randint(0, 3))
	data = driver.find_elements_by_css_selector(".mod g-link a")
	music_data = driver.find_elements_by_css_selector("div[class='scrt'] a")
	social_links = []
	social_links.append(name)

	with open("database.csv", "a", newline="") as cf:
		writer = csv.writer(cf, delimiter="|", )
		for music in music_data:
			social_links.append(music.get_attribute("text"))
			social_links.append(music.get_attribute("href"))
			print(music.get_attribute("text"), music.get_attribute("href"))
	
		for link in data:
			social_links.append(link.get_attribute("text"))
			social_links.append(link.get_attribute("href"))
			print(link.get_attribute("text"), link.get_attribute("href"))
		writer.writerow(social_links)
