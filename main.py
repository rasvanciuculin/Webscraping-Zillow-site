import time
from zillow_listing import ZillowSearchListing
from update_form import UpdateForm

Google_sheet = "https://docs.google.com/spreadsheets/d/1zrkaoXYbCbBWl8W-SYyo-CsZuSWmvArGVHJB7W-iGbo/edit?usp=sharing"
Google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLScNGWQ3oY8amxYIf89bcwliL-hD5Q3D9fXYOTKVq8_ZR_WMDQ/viewform?usp=sharing"

zillow_url ="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
            "mapBounds%22%3A%7B%22north%22%3A37.88836615784793%2C%22south%22%3A37.66204454350355%2C%22east%22%3A" \
            "-122.23248568896484%2C%22west%22%3A-122.63417331103516%7D%2C%22regionSelection%22%3A%5B%7B%22" \
            "regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState" \
            "%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc" \
            "%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22" \
            "value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue" \
            "%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu" \
            "%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2400%7D%2C%22price%22%3A%7B%22max" \
            "%22%3A504262%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

nr_pages = int(input("There are 40 rental ads per page. How many pages to save in a file? "))

""" Get url for every page on Zillow search"""

url_list = []
for url_num in range(1, nr_pages):
    if url_num != 1:
        change_url = f"{zillow_url[:48]}{url_num}_p/{zillow_url[48:92]}22currentPage%22%3A{url_num}%{zillow_url[92:]}"
        url_list.append(change_url)
    else:
        url_list.append(zillow_url)

complete_address_list = []
complete_price_list = []
complete_link_list = []

page_url = 1

""" For every page in the Zillow search get the data for link, price and address"""

for url in url_list:
    print(page_url)
    time.sleep(3)
    z = ZillowSearchListing(url)
    z.make_soup()
    z.zillow_search()
    for link in z.link_list:
        complete_link_list.append(link)
    for price in z.price_list:
        complete_price_list.append(price)
    for address in z.address_list:
        complete_address_list.append(address)

    page_url += 1

form = UpdateForm(Google_form_link)
form.update_form(complete_address_list, complete_price_list, complete_link_list)
sheet = UpdateForm(Google_sheet)





