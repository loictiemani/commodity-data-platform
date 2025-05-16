import requests
from bs4 import BeautifulSoup

def scrape_oil_news():
    url = "https://www.oilprice.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h4')
    news = [h.text.strip() for h in headlines if h.text.strip() != '']
    
    with open("/tmp/oil_news.txt", "w") as f:
        for item in news:
            f.write(item + "\n")
    print("✅ News scraped to /tmp/oil_news.txt")