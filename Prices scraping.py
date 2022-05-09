from bs4 import BeautifulSoup
import requests
import pandas as pd

url_alimentos = "https://www.supermercadoluxor.com/product-category/alimentos/"
max_pages = 20
count = 0
req = requests.get(url_alimentos, headers={"User-Agent": "XY"})
statusCode = req.status_code