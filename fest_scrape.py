from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://visitindiana.com/events?sort=distance-location&cat=5%2C7%2C8&miles=50&location=40203').text

soup = BeautifulSoup(source, 'lxml')

# csv_file = open('festival_in_19.csv', 'w')
# csv.writer = csv.writer(csv_file)
# csv.writer.writerow(['event', 'local', 'date'])

event = soup.find('div', class_="content")

print(event.prettify())