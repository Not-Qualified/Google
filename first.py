from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv


driver = webdriver.Chrome("chromedriver")
driver.get("http://google.com/search?q=selena+gomez")
# driver.get("https://google.com/search?q=Best+Hollywood+Celebrities")
count = 0

while True:

	# Getting Links
	# time.sleep(random.randint(0, 2))
	# data = driver.find_elements_by_css_selector(".mod g-link a")
	# for link in data:
	# 	print(link.get_attribute("href"))
	# input()
	
	def sidebar():
		# Sidebar People also Search For
		child = random.randint(1, 3)
		people = driver.find_element_by_css_selector(f"div[data-reltype='sideways']:nth-child({child}) > a").click()
		name = driver.find_element_by_css_selector("input[name='q']").get_attribute("value")
		print(name)

		# Getting Data
		global count
		count += 1
		time.sleep(random.randint(0, 2))
		data = driver.find_elements_by_css_selector(".mod g-link a")
		music_data = driver.find_elements_by_css_selector("div[class='scrt'] a")
		social_links = []
		social_links.append(name)

		with open("first.csv", "a", newline="") as cf:
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



	def top():
		# Top Cards - People also Search For
		people = driver.find_elements_by_css_selector('div[id="extabar"] g-scrolling-carousel div[role="list"] a')
		people[random.randint(1, 15)].click()
		name = driver.find_element_by_css_selector("input[name='q']").get_attribute("value")
		print(name)

		# Getting Data
		global count
		count += 1
		time.sleep(random.randint(0, 2))
		data = driver.find_elements_by_css_selector(".mod g-link a")
		music_data = driver.find_elements_by_css_selector("div[class='scrt'] a")
		social_links = []
		social_links.append(name)

		with open("first.csv", "a", newline="") as cf:
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


	lst = [sidebar, top]
	try:
		random.choice(lst)()
	except:
		pass

	try:
		random.choice(lst)()
	except:
		pass

	try:
		random.choice(lst)()
	except:
		pass

	print(count)

	time.sleep(random.randint(1, 5))


driver.close()




























# data = driver.find_element_by_css_selector(".mod div[data-original-name='Lauren Hashian']").text
# url = driver.find_element_by_css_selector("div[data-reltype='sideways']:nth-child(1) > a").get_attribute("href")

#data = driver.find_element(By.CSS_SELECTOR, "g-link a").get_attribute("href")

# data = driver.find_elements(By.CSS_SELECTOR, "g-link a")

# driver.get(people)

# data = driver.find_element_by_css_selector("g-link a").get_attribute("href")


# for person in people:
	# 	# driver.get(person.get_attribute("href"))
	# 	print(person.get_attribute("href"))
	# 	# person.click()
	# 	# time.sleep(3)