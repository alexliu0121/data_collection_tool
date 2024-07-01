import requests
from bs4 import BeautifulSoup

def fetch_social_media_trends(config):
    url = config['url'] + '?query=' + config['query'] + '&max_results=' + str(config['max_results'])
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Assume we are extracting a list of social media posts
    data = []
    posts = soup.find_all('div', {'class': 'post'})
    for post in posts:
        data.append({
            'user': post.find('span', {'class': 'user'}).text.strip(),
            'content': post.find('p', {'class': 'content'}).text.strip(),
            'date': post.find('span', {'class': 'date'}).text.strip()
        })
    return data
