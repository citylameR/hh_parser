import lxml as lxml
import json
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint

# TODO ссылка+, вилка зп+, название компании+, город+
if __name__ == "__main__":
    headers = Headers(os="mac", headers=True).generate()

data_company = [{
    'link' : 'link',
    'sity' : 'sity',
    'sallary' : 'sallary',
    'company': 'company'
}]

response_text = requests.get(
    'https://spb.hh.ru/search/vacancy?area=1&area=2&search_field=description&only_with_salary=true&text=Python+django+flask&from=suggest_post&ored_clusters=true&enable_snippets=true',
    headers=headers).text
soup = BeautifulSoup(response_text, features='lxml')


def find_link(soup):
    link = soup.find_all(class_="serp-item__title")
    for l in link:
        LH = l['href']
        print(LH)


def find_sity(soup):
    sity = soup.find_all(attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
    for s in sity:
        print(s.text)


def find_sallary(soup):
    sallary = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
    for sall in sallary:
        print(sall.text)


def find_company(soup):
    company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})
    for c in company:
        print(c.text)

    with open('hh.json', 'w') as file:
        data = json.load()

#=======================================================================================================================

link = soup.find_all(class_="serp-item__title")
sity = soup.find_all(attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
for l in link:
    LH = l['href']
    for s in sity:
        data_company.append({
            "link" : LH,
            'sity' : s.text
        })
    break

pprint(data_company)






# sallary = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
# for sall in sallary:
#     print(sall.text)
#
# company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})
# for c in company:
#     print(c.text)
























# company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})
# for c in company:
#     data = c.text
#     print(data)
#     data_company.append({'company': data})


