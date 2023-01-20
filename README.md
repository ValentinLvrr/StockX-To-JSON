![banner](https://d2hlo835aj7uqe.cloudfront.net/production/wp-content/uploads/2021/04/Blog-social-v1.jpg)

# Installation & Configuration
### 1: Clone the repository
```
git clone https://github.com/ValentinLvrr/StockX-To-JSON
cd Geev-Bot
```

### 2: Add links or name to [`objects.txt`](https://github.com/ValentinLvrr/StockX-To-JSON/blob/main/objects.txt)
```
https://stockx.com/fr-fr/sony-ps5-playstation-5-digital-edition-console-white
dunk low homer
https://stockx.com/fr-fr/swatch-x-omega-bioceramic-moonswatch-mission-to-jupiter-so33c100-brown
jordan chicago
```

### 3: Customize or not the delay and the files in [`config.py`](https://github.com/ValentinLvrr/StockX-To-JSON/blob/main/config.py)
```py
class Delay:
    isEnabled = True
    time = 0.1

class Files:
    links = 'objects.txt'
    output = 'output.json'
```
# Launching
```
python3 stockx.py
```

# Result

### Terminal :
```
✅ | sony ps5 playstation 5 digital edition console white
✅ | dunk low homer
✅ | swatch x omega bioceramic moonswatch mission to jupiter so33c100 brown
✅ | jordan chicago
📝 | 4 written in output.json!
```
### [`output.json`](https://github.com/ValentinLvrr/StockX-To-JSON/blob/main/output.json) :
```json
{
      "product": {
        "name": "Next Nature Homer Simpson (GS)",
        "brand": "Nike",
        "gender": "child",
        "category": "Dunk Low",
        "colorway": "Blue Chill/Yellow/Strike-White",
        "imageUrl": "https://images.stockx.com/images/Nike-Dunk-Low-Next-Nature-Home-Simpson-GS-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&trim=color&q=90&dpr=2&updated_at=1657198087"
      },
      "bid_ask_data": {
        "lowestAsk": 94,
        "lowestAskSize": "",
        "numberOfAsks": 440,
        "highestBid": 110,
        "highestBidSize": "",
        "numberOfBids": 56
      },
      "sales_informations": {
        "lastSale": 83,
        "salesLast72Hours": 24
      }
    },
```

