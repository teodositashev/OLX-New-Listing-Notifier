import requests

from bs4 import BeautifulSoup
from typing import List, Tuple, Optional

def scrape_info(url: str) -> List[Tuple[str, str, str]]:
    """Scrape information from a specified OLX URL."""

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    scraped_info = []

    ad_cards = soup.findAll("div", attrs={"data-cy": "ad-card-title"})

    for ad_card in ad_cards:

        title_tag = ad_card.find("h6", class_="css-1wxaaza")
        title = title_tag.get_text(strip=True)

        price_tag = ad_card.find("p", class_="css-13afqrm")
        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "Price not available"
        
        link_tag = ad_card.find("a", class_="css-z3gu2d")
        if link_tag and 'href' in link_tag.attrs:
            link = "https://www.olx.bg" + link_tag['href']
        
        scraped_info.append((title, price, link))
        
    return scraped_info