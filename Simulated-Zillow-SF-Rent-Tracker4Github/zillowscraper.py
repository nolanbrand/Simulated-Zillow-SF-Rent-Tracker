import requests
from bs4 import BeautifulSoup
import lxml
import re

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


class ZillowScraper:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_CLONE_URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, "lxml")
        self.rentals = self.soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    def get_all_prices(self):
        prices_list = [rental.span.text for rental in self.rentals]

        for i in range(len(prices_list)):
            if "+" in prices_list[i]:
                prices_list[i] = prices_list[i].split("+", 1)[0]
            else:
                prices_list[i] = prices_list[i].split("/", 1)[0]

        return prices_list

    def get_all_links(self):
        links_list = [rental.a["href"] for rental in self.rentals]

        return links_list

    def get_all_addresses(self):
        address_list = [rental.address.text.strip() for rental in self.rentals]

        for i in range(len(address_list)):
            address_list[i] = re.sub(r'^.*?[|,]', " ", address_list[i]).strip()

        return address_list
