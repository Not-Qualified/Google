from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
import base64
from pathlib import Path


driver = webdriver.Chrome("chromedriver")

file = open("list.txt", "r")
lines = file.readlines()
for line in lines:
	driver.get(f"http://google.com/search?q={line}")
		
	try:
		title_name = driver.find_element_by_css_selector("h2[data-attrid='title'] span").text
		subtitle = driver.find_element_by_css_selector("div[data-attrid='subtitle'] span").text
	except:
		title_name = driver.find_element_by_css_selector("input[name='q']").get_attribute("value")
		subtitle = "None"


	print(title_name, " - ", subtitle)
	
	time.sleep(random.randint(0, 3))
	data = driver.find_elements_by_css_selector(".mod g-link a")
	music_data = driver.find_elements_by_css_selector("div[class='scrt'] a")
	social_links = []
	# social_links.append(name)
	social_links.append(title_name, )
	social_links.append(subtitle, )


	# Saving Image
	try:
		file_name = f"{title_name} - {subtitle}.jpg"
		path = Path(__file__).parent / f"img/{file_name}"
		image = driver.find_element_by_css_selector("div[data-attrid='image'] img").get_attribute("src").split(",")[1].replace(' ', '+')
		img_data = base64.b64decode(image)

		with path.open("wb") as f:
			f.write(img_data)
			f.close()
	except:
		file_name = None

	if(file_name == None):
		try:
			file_name = f"{title_name} - {subtitle}.jpg"
			path = Path(__file__).parent / f"img/{file_name}"
			image = driver.find_element_by_css_selector("g-img[data-attrid='image'] img").get_attribute("src").split(",")[1].replace(' ', '+')
			img_data = base64.b64decode(image)

			with path.open("wb") as f:
				f.write(img_data)
				f.close()
		except:
			file_name = "None"

	social_links.append(file_name)

	


	with open("new.csv", "a", newline="") as cf:
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

driver.close()