from bs4 import BeautifulSoup
import requests
import time

from datetime import date
current_year = date.today().year

html_text = requests.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Casa.aspx').text
soup = BeautifulSoup(html_text, 'lxml')
tabla_tarifas = soup.find('div', class_ = 'col-xs-12')
tipos = tabla_tarifas.find_all('a')

nombre = []
url_completo = []

for index, tipo in enumerate(tipos):
    nombre.append(tipo.text)
    url = tipo['href'].replace('..', '')
    url_completo.append('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas' + url)



html_2 = requests.get(url_completo[0]).text
soup2 = BeautifulSoup(html_2, 'lxml')
year = soup2.find('select', class_ = 'input').text

for year ==

