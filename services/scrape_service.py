import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

def scrapeContent(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    entityListMeta = soup.find('div', class_='entity-list-meta')
    itemCount = entityListMeta.find('strong', class_='entities-count').text.strip()

    return int(itemCount)

def scrapeContentPaginated(urls):
    for url in urls:
        print(url)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles = soup.find_all('article', class_='entity-body cf')
        filteredContent = []
        for article in articles:
            h3 = article.find('h3', class_='entity-title')
            name = h3.find('a', class_='link') 

            price = article.find('strong', class_ = 'price price--hrk')

            if None not in (name, price):
                filteredContent.append([name.text.strip(), price.text.strip()[:-3]])    
    return filteredContent
