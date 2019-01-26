from lxml import html
from requests import get
from bs4 import BeautifulSoup

url = "https://www.indeed.fi/jobs?q=operations&l=Vaasa"
headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

jobs_link  = html_soup.find_all('div',class_ = "jobsearch-SerpJobCard row result clickcard")
print(jobs_link)
