import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.web_scraper import scrape_oil_news

scrape_oil_news()