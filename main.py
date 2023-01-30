import lxml as lxml
import json
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint

# TODO ссылка+, вилка зп+, название компании+, город+
if __name__ == "__main__":
    headers = Headers(os="mac", headers=True).generate()

data_company = []

response_text = requests.get(
    'https://spb.hh.ru/search/vacancy?area=1&area=2&search_field=description&only_with_salary=true&text=Python+django'
    '+flask&from=suggest_post&ored_clusters=true&enable_snippets=true',
    headers=headers).text
soup = BeautifulSoup(response_text, features='lxml')


link = soup.find_all(class_="serp-item__title")
city = soup.find_all(attrs={'class': "bloko-text", 'data-qa': "vacancy-serp__vacancy-address"})
sallary = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-compensation"})
company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})


for l, s, sall, c in zip(link, city, sallary, company):
    data_company.append(
        {
            'link' : l['href'],
            'city' : s.text,
            'sallary': sall.text,
            'company' : c.text
        }
    )


with open('hh.json', 'w', encoding='utf-8') as file:
    json.dump(data_company, file, indent=4, ensure_ascii=False)


pprint(data_company)




























# company = soup.find_all(attrs={'data-qa': "vacancy-serp__vacancy-employer"})
# for c in company:
#     data = c.text
#     print(data)
#     data_company.append({'company': data})


