from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

#years = [0, 0]
#
#from datetime import date
#current_year = date.today().year
#years[0] = str(current_year)
#last_year = current_year - 1
#years[1] = str(last_year)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Tarifas/Tarifa1.aspx")

year_options = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))

for h in range(0, len(year_options.options)):
    select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
    select_year.select_by_index(h)
    month_options = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_MesVerano1_ddMesConsulta'))

    for i in range(1, len(month_options.options)):
        select_month = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_MesVerano1_ddMesConsulta'))
        time.sleep(1)
        select_month.select_by_value(f'{i}')

        table = driver.find_element(By.ID, 'ContentPlaceHolder1_TemporadaFV')
        rangos = table.find_elements(By.TAG_NAME, 'tr')

        for rango in rangos[2:]:
            x = rango.find_elements(By.TAG_NAME, 'td')
            for y in x:
                print(y.text)