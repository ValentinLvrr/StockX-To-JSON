from config import DELAY, LINKS_FILE ,OUTPUT_FILE
from time import sleep
import requests
import json

saved = {"sneakers" : [],}

def add(item):
    
    """
    Add Item to a list
    """
    saved['sneakers'].append({
        "product": {
            "name": item['name'],
            "brand": item['brand'],
            "gender": item['gender'],
            "category": item['category'],
            "colorway": item['colorway'],
            "imageUrl": item['imageUrl']
        },
        "bid_ask_data": {
            "lowestAsk": item['lowestAsk'],
            "lowestAskSize": item['lowestAskSize'],
            "numberOfAsks": item['numberOfAsks'],
            "highestBid": item['highestBid'],
            "highestBidSize": item['highestBidSize'],
            "numberOfBids": item['numberOfBids']
        },
        "sales_informations" : {
            "lastSale": item['lastSale'],
            "salesLast72Hours": item['salesLast72Hours']
        }
    })

def search(query):
    """
    Getting Product Informations from
    the StockX Api
    """

    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'app-platform': 'Iron',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    res = requests.get(url, headers=headers)

    if res.ok:

        data = res.json()
        product = data['Products'][0]
        market = product['market']
        
        stockx_item = {
            "name": product['name'],
            "brand": product['brand']   ,
            "gender": product['gender']  ,
            "category" : product['category'],
            "colorway" : product['colorway'],
            "imageUrl" : product['media']['imageUrl'],

            "lowestAsk" : market['lowestAsk'],
            "lowestAskSize" : market['lowestAskSize'],
            "numberOfAsks" : market['numberOfAsks'],
            "highestBid" : market['highestBid'],
            "highestBidSize" : market['highestBidSize'],
            "numberOfBids" : market['numberOfBids'],

            "lastSale" : market['lastSale'],
            "salesLast72Hours" : market['salesLast72Hours']
        }

        add(item=stockx_item)
        
        if 'https://stockx.com/' in query:
            print("✅ " + query.split('/')[-1].replace('-',' '))
        else:
            print("✅ " + query)

        sleep(DELAY)

    else:
        print(f"✴️ request error: ({res.status_code})")

if __name__ == "__main__":

    links = open(LINKS_FILE,'r').readlines()
    for url in links:
        search(url.strip())

    # Writting
    json_object = json.dumps(saved, indent=2)
    open(OUTPUT_FILE, "w").write(json_object)

    print(f"📝 {len(saved['sneakers'])} written in {OUTPUT_FILE}!")
    input()