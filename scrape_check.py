import requests
from bs4 import BeautifulSoup

url = "https://www.family.co.jp/goods/snack.html"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

products = soup.select(".c-product-list__item")
print(f"商品数: {len(products)}")

# 最初の1件だけ表示
if products:
    print(products[0].prettify())
else:
    print("商品が見つかりませんでした。")