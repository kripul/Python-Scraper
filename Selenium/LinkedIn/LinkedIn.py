from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=2')
print('Scraping LinkedIn is an ilegal activity, please doing with your own risk! \nDont use your personal account for scraping!')
email = input("Enter your email : ")
passw = input("Enter your password : ")

driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key')
sleep(5)
username.send_keys(email)
password = driver.find_element_by_id('session_password')
sleep(5)
password.send_keys(passw)
loginbutton = driver.find_element_by_class_name('sign-in-form__submit-button')
sleep(5)
loginbutton.click()

with open('gresult.txt', 'r') as f:
	for url in f.read().splitlines():
		driver.get(url)
		print('scraping url ' + url)
		sleep(10)
		soup_a = BeautifulSoup(driver.page_source, 'html.parser')
		name = soup_a.select_one('li.inline.t-24.t-black.t-normal.break-words')
		name = name.text.strip() if name else "N/A"
		job = soup_a.select_one('.mt1.t-18.t-black.t-normal.break-words')
		job = job.text.strip() if job else "N/A"
		location = soup_a.select_one('li.t-16.t-black.t-normal.inline-block')
		location = location.text.strip() if location else "N/A"

		experiences = soup_a.select('.text-align-left.ml2.t-14.t-black.t-bold.full-width.lt-line-clamp.lt-line-clamp--multi-line.ember-view.text-align-left.ml2.t-14.t-black.t-bold.full-width.lt-line-clamp.lt-line-clamp--multi-line.ember-view')
		if len(experiences) == 1:
		    company = experiences[0].text.strip() if experiences[0] else "N/A"
		elif len(experiences) == 2:
		    company = experiences[0].text.strip() if experiences[0] else "N/A"
		    university = experiences[1].text.strip() if experiences[1] else "N/A"
		else:
		    company = "N/A"
		    university = "N/A"
		with open('lresult.csv', 'a', encoding='utf-8', newline='') as f:
			writer= csv.writer(f)
			writer.writerow([name,job,location,company,university,url])