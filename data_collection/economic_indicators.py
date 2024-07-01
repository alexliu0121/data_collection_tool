import requests
from bs4 import BeautifulSoup

def fetch_economic_indicators(config):
    response = requests.get(config['url'])
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Assume we are extracting a table of economic indicators
    data = []
    table = soup.find('table', {'id': 'economic-indicators-table'})
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            data.append({
                'indicator': columns[0].text.strip(),
                'value': columns[1].text.strip(),
                'date': columns[2].text.strip()
            })
    return data
