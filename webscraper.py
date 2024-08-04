import json
import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.scrapethissite.com/pages/simple')
response=response.text

parse=BeautifulSoup(response, 'html.parser')

country_divs=parse.select('div.country')
country_data=[]

for country_div in country_divs:
    countryName = country_div.select_one('h3.country-name').text.strip()
    countryPop = country_div.select_one('span.country-population').text.strip()
    country_data.append({
        'Country Name': countryName,
        'Country Population': countryPop
    })

print(json.dumps(country_data, indent=2))
