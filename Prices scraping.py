from bs4 import BeautifulSoup
import requests
import pandas as pd

url_alimentos = "https://www.supermercadoluxor.com/product-category/alimentos/"
max_pages = 20
counter = 0
df_alimentos = pd.DataFrame({'Titulo':[],
                   'Precio':[]})
req = requests.get(url_alimentos, headers={"User-Agent": "XY"})
statusCode = req.status_code

for i in range(1, max_pages):
    
    if i > 1:
        url = "%sPage/%d/" % (url_alimentos, i)
    else:
        url = url_alimentos
        
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        
        entradas = html.find_all('ul', {'class': 'products columns-4'})
        
        for entrada in entradas:
            listas = html.find_all('li')
            
            for lista in listas:
                counter +=1
                titulo = lista.find('span', {'class':'woocommerce-Price-amount amount'}).getText()
                precio = lista.findfind('span', {'class':'woocommerce-Price-amount amount'}).getText()
                
                df_alimentos = df_alimentos.append({'Titulo': titulo,
                                'Precio': precio},
                               ignore_index=True)
                
    else:
        break