import csv

# with open("first.csv", "a", newline="") as cf:
# 	fieldnames = ["name", "age"]
# 	writer = csv.DictWriter(cf, delimiter='|', fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)

# 	writer.writeheader()
# 	writer.writerow({"name": "Alexa", "age": 5})
# 	writer.writerow({"name": "Alexa", "age": 5})
# 	writer.writerow({"name": "Alexa", "age": 5})
# 	writer.writerow({"name": "Alexa", "age": 5})

# 	cf.close()


with open("first.csv", "a", newline="") as cf:
	writer = csv.writer(cf, delimiter="|", )
	writer.writerow(["First", "Second", "Third"])
	writer.writerow(["First", "Second", "Third"])
	writer.writerow(["First", "Second", "Third"])
	writer.writerow(["First", "Second", "Third"])
	writer.writerow(["First", "Second", "Third"])