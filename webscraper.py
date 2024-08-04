import requests
from bs4 import BeautifulSoup

def fetch_population_data(url):
    #get request
    response = requests.get(url)
    
    #verify successful get request
    if response.status_code != 200:
        print("Failed to retrieve data")
        return
    
    #use this beautfulsoup library which required a lot of time reading documentation
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #this line just looks for a table.
    data_table = soup.find('table')
    
    #extracts the data from the table on wikipedia
    countries_population = []
    rows = data_table.find_all('tr')
    
    for row in rows[1:]:  
        cols = row.find_all('td')
        country = cols[0].text.strip()
        population = cols[1].text.strip()
        countries_population.append((country, population))
    
    return countries_population

def print_population_data(countries_population):
    #this creates the readable output. Took forever to figure out.
    print(f"{'Country':<25} {'Population':>15}")
    print("="*40)
    for country, population in countries_population:
        print(f"{country:<25} {population:>15}")

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
    data = fetch_population_data(url)
    
    if data:
        print_population_data(data)

