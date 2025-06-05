from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.lawson.co.jp/recommend/new/")
time.sleep(5)  # JavaScriptの読み込み待ち（確実に待つ）

# 画面上のすべての「li」タグのテキストを取得
lis = driver.find_elements("tag name", "li")
print(f"liタグ数: {len(lis)}")

for li in lis[:10]:  # 最初の10個だけ表示（確認用）
    print("--------")
    print(li.text)

driver.quit()