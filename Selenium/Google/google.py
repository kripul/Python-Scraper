from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent #pip install fake-useragent
import time

ua = UserAgent()
user_agent = ua.random
PROXY = '38.91.100.122:3128' #please use your own HTTP proxy
use_proxy = False #change to True if you want use proxy

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('log-level=2')
if use_proxy == True:
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
else:
    None
driver = webdriver.Chrome(options=chrome_options)



def search():
    with open('query.txt', 'r') as f, open('result.txt', 'w') as writer:
        for line in f.read().splitlines():
            print('searching with query ' + line)
            url = 'https://www.google.com/search?num=100&q=' + line
            driver.get(url)
            time.sleep(5)
            try:
                urls = driver.find_elements_by_xpath('//*[@class="r"]/a')
                for url in urls:
                    writer.write(url.get_attribute('href')+ '\n')
                    print(url.get_attribute('href'))
            except:
                print('failed get links')
    driver.quit()

search()