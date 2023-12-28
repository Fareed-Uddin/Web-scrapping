import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings('ignore', category=InsecureRequestWarning)

service = Service()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://oxylabs.io/blog')


results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

for a in soup.findAll(class_='css-4g6ai3 e1dscegp0'):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(class_='css-4g6ai3 e1dscegp0'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')