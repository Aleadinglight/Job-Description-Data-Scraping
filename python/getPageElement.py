from lxml import html
from requests import get
from bs4 import BeautifulSoup

def getContent(url="", headers=""):
    url = "https://www.indeed.com/viewjob?jk=1fedc0d304417c06&tk=1d2105cgi5hhb804&from=serp&vjs=3"
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    print(url)
    print(headers)
    response = get(url, headers=headers)

    # print(response.text[:100])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    jobs_desc = html_soup.find_all('p')

    jobs_desc_str = ''
    # Remove all the html tag from the result
    for i in range(0, len(jobs_desc)):
        jobs_desc_str+= '\n'+str(jobs_desc[i].string)
    return jobs_desc_str
