from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Chromeドライバーのパス
service = Service('chromedriver.exe')  # ここを環境に合わせて変更
driver = webdriver.Chrome(service=service)

url = "https://www.lawson.co.jp/recommend/new/"
driver.get(url)

# JavaScriptの読み込み待機（必要に応じて調整）
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

items = []
for product in soup.select(".itemList li"):
    name_tag = product.select_one(".ttl")
    date_tag = product.select_one(".date")
    
    if name_tag and date_tag:
        items.append({
            "商品名": name_tag.get_text(strip=True),
            "発売日": date_tag.get_text(strip=True)
        })

driver.quit()

# 出力
os.makedirs("output", exist_ok=True)
df = pd.DataFrame(items)
df.to_csv("output/lawson_selenium.csv", index=False, encoding="utf-8-sig")

print("SeleniumでのCSV出力完了！")