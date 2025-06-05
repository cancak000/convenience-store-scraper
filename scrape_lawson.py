import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.lawson.co.jp/recommend/new/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

items = []

for product in soup.select(".itemList li"):
    name_tag = product.select_one(".ttl")
    date_tag = product.select_one(".date")
    
    if name_tag and date_tag:
        items.append({
            "商品名": name_tag.get_text(strip=True),
            "発売日": date_tag.get_text(strip=True)
        })

# CSV出力
os.makedirs("output", exist_ok=True)
df = pd.DataFrame(items)
df.to_csv("output/lawson_new_items.csv", index=False, encoding="utf-8-sig")

print("CSV出力完了（ローソン）")