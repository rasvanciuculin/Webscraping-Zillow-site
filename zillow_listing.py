import requests
import json
from bs4 import BeautifulSoup

zillow_url ="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%" \
            "7D%2C%22" \
            "mapBounds%22%3A%7B%22north%22%3A37.88836615784793%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37" \
            ".662044543503555%2C%22west%22%3A-122.63417331103516%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A" \
            "%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22" \
            "value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C" \
            "%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%" \
            "3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2400%7D%2C%22price%22%3A%7B%22max%22%3A503882%7D%2C%22beds%22%3A%7" \
            "B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%" \
            "22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

class ZillowSearchListing:

    """ This class parse data from https://www.zillow.com """

    def __init__(self, url):
        self.url = url
        self.soup = self.make_soup()
        self.link_list = []
        self.price_list = []
        self.address_list = []

    def make_soup(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
            "Accept-Language": "en-US,en;q=0.5"
        }
        response = requests.get(url=self.url, headers=headers)
        return BeautifulSoup(response.content, "html.parser")

    def zillow_search(self):

        """ Get the lists for link, price and address on a single zillow page."""

        soup = self.soup
        data = json.loads(
        soup.find("script", attrs={"data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip('<!->'))
        all_data = data["cat1"]["searchResults"]["listResults"]
        # print(json.dumps(all_data, indent=4))
        for result in all_data:
            if "http" not in result["detailUrl"]:
                self.link_list.append(f"https://www.zillow.com{result['detailUrl']}")
            else:
                self.link_list.append(result["detailUrl"])
            try:
                self.price_list.append(result["unformattedPrice"])
            except KeyError:
                price = result["units"][0]["price"].replace(",", "").split("$")[1].split("+")[0]
                self.price_list.append(int(price))
            self.address_list.append(result["address"])