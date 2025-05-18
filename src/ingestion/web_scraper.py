import requests
from bs4 import BeautifulSoup
import os

def scrape_oil_news():
    url = "https://www.oilprice.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # raise exception on HTTP error
    except requests.RequestException as e:
        print(f"❌ Failed to fetch data: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h4')
    news = [h.text.strip() for h in headlines if h.text.strip()]
    
    if not news:
        print("⚠️ No headlines found. Website structure may have changed.")
        return

    with open("/tmp/oil_news.txt", "w") as f:
        for item in news:
            f.write(item + "\n")
    print("✅ News scraped to /tmp/oil_news.txt")