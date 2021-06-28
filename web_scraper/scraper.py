import requests
import json
from bs4 import BeautifulSoup

Url='https://en.wikipedia.org/wiki/History_of_Mexico'
def get_citations_needed_count(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    cout_elements = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(cout_elements)


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact') 
    phrags = []


    for ele in results:
        if ele not in phrags:
            phrags.append(ele.findParent().text.strip())

    phrags = list(dict.fromkeys(phrags))


    file_content = json.dumps(phrags)
    with open('all_jobs.json', 'w') as file:
        file.write(file_content)
    return ''.join(phrags)





print (get_citations_needed_count(Url))
print(get_citations_needed_report(Url))