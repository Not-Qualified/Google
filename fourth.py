from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random



driver = webdriver.Chrome("chromedriver")
# driver.get("http://google.com/search?q=the+rock")
driver.get("https://google.com/search?q=Best+People+in+the+world")
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

		# Getting Data
		global count
		count += 1
		time.sleep(random.randint(0, 2))
		data = driver.find_elements_by_css_selector(".mod g-link a")
		for link in data:
			print(link.get_attribute("href"))



	def top():
		# Top Cards - People also Search For
		people = driver.find_elements_by_css_selector('div[id="extabar"] g-scrolling-carousel div[role="list"] a')
		people[random.randint(1, 15)].click()

		# Getting Data
		global count
		count += 1
		time.sleep(random.randint(0, 2))
		data = driver.find_elements_by_css_selector(".mod g-link a")
		for link in data:
			print(link.get_attribute("href"))


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





	# time.sleep(random.randint(0, 5))



	time.sleep(2)


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