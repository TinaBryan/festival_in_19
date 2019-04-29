#
# from bs4 import BeautifulSoup
import re
import requests
import csv

source = requests.get('https://visitindiana.com/events?sort=distance-location&cat=5%2C7%2C8&miles=50&location=40203').text

titleRE = re.compile(r"<h3><a href=\"events\/(?:.*?)\"><span itemprop=\"name\">(.*?)<\/span><\/a><\/h3>")

# soup = BeautifulSoup(source, 'lxml')

# csv_file = open('festival_in_19.csv', 'w')
# csv.writer = csv.writer(csv_file)
# csv.writer.writerow(['event', 'local', 'date'])

# event = soup.find_all('div', class_="content")

titles = re.findall(titleRE, source)
for title in titles:
    print(title)