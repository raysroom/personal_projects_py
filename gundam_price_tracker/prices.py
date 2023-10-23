# Ver 1.2 *Added Store class and get_store method*
""" Usage:
    Valid command-line arguments:
        'compare', 'newtype', 'usags' """
import requests, csv, sys, re
from bs4 import BeautifulSoup
from tabulate import tabulate

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

class Store:
    file = 'gundam.csv'
    @classmethod
    def get_store(cls, store):
        products = []
        with open(f'{cls.file}') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({"Product": row["kit"], "URL": row[f"{store}"]})
        return products
    
   
def newtype_prices(store_name):
    store = Store.get_store(store_name)
    product_list = []
    for product in store:
        item = product["Product"]
        URL = product["URL"]
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        
        stock = soup.find('div', class_='stock-tag').get_text()
        stock = stock.strip().replace('\n','')

        price = soup.find('div', class_='items-start').get_text()
        price = price.replace(' ', '')
        price = price.strip().replace('\n', ', ')
        price = price.replace(', ,',',')
        
        product_list.append({"Newtype - Kit": item, "Price": price, "Stock": stock})
    
    print(tabulate(product_list, headers = "keys", tablefmt="simple_outline"))
    print("https://newtype.us/")
    
def usags_prices(store_name):
    store = Store.get_store(store_name)
    product_list = []
    for product in store:
        item = product["Product"]
        URL = product["URL"]
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')

        stock = soup.find(id = 'btn').get_text()
        if "sold out" in stock.lower():
            stock = "Out of Stock"
        else:
            stock = "In Stock"

        price = soup.find('div', class_='price--large').get_text()
        remove = [' ', '\n']
        for char in remove:
            price = price.replace(char, '')
        
        #formatted digits with a ? to find the price of kits that have over 3 digits
        #eg. $120 kit vs a $60 kit
        prices = re.search(r"Regularprice(\$\d\d\d?.\d\d)(?:Regularprice)?(\$\d\d\d?.\d\d)?", price)
        price = prices.group(1)
        
        product_list.append({"USAGS - Kit": item, "Price": price, "Stock": stock})
        
    print(tabulate(product_list, headers = "keys", tablefmt="simple_outline"))
    print("https://www.usagundamstore.com/")

def main():
    try:
        site = sys.argv[1]
        if site == 'compare':
            newtype_prices("newtype")
            usags_prices("usags")
        elif site == 'newtype':
            newtype_prices(site)
        elif site == 'usags':
            usags_prices(site)
        else:
            raise IndexError
    except IndexError:
        sys.exit('Provide command: "compare", "newtype", or "usags"')

if __name__ == "__main__":
    main()