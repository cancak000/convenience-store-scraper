import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.family.co.jp/goods/snack.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

items = []

for item in soup.select('.ly-mod-layout .c-product-list__item'):
    name = item.select_one('.c-product-list__item-title')
    price = item.select_one('.c-product-list__item-price')

    if name and price:
        items.append({
            '商品名': name.text.strip(),
            '価格': price.text.strip()
        })

df = pd.DataFrame(items)
df.to_csv('output/famima_snacks.csv', index=False, encoding='utf-8-sig')

print("CSV出力完了")
