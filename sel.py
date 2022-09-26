from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import csv
import time
import wx
#import x


#class UI(x.Mywin):
#    def __init__(self, parent):
#        x.Mywin.__init__(self, parent)

def CFE():
    # Accesar al driver y actions
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    actions = ActionChains(driver)

    funciones = {
        "HOGAR": HOGAR,
        "NEGOCIO": NEGOCIO,
    }

    D_meses = {
        'ENERO': 1,
        'FEBRERO': 2,
        'MARZO': 3,
        'ABRIL': 4,
        'MAYO': 5,
        'JUNIO': 6,
        'JULIO': 7,
        'AGOSTO': 8,
        'SEPTIEMBRE': 9,
        'OCTUBRE': 10,
        'NOVIEMBRE': 11,
        'DICIEMBRE': 12
    }

    S_servicio = input('Servicio: ').upper()
    S_tarifa = input('Tarifa: ').upper()
    S_anio = input('Año: ').upper()
    S_mes = input('Mes: ').upper()

    if S_mes == 'TODOS':
        pass
    else:
        S_mes = str(D_meses[S_mes])


    for key, val in funciones.items():
        if key == S_servicio:
            val(driver, actions, S_tarifa, S_anio, S_mes)
        else:
            pass


def HOGAR(driver, actions, S_tarifa, S_anio, S_mes):
    driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Casa.aspx')

    opciones_tarifas = driver.find_elements(By.XPATH, "//div[@class='col-xs-12']/p/a")

    templist = []
    templist2 = []

    if S_tarifa == 'TODAS':
        for index, val in enumerate(opciones_tarifas):
            try:
                opciones_tarifas = driver.find_elements(By.XPATH, "//div[@class='col-xs-12']/p/a")
                actions.move_to_element(opciones_tarifas[index]).perform()
                opciones_tarifas[index].click()

                cuales_anios(driver, templist, templist2, S_anio, S_mes)
                driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Casa.aspx')
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='col-xs-12']/p/a")))
            except StaleElementReferenceException:
                pass
    else:
        try:
            opciones_tarifas = driver.find_element(By.PARTIAL_LINK_TEXT, S_tarifa)
            actions.move_to_element(opciones_tarifas).perform()
            opciones_tarifas.click()

            cuales_anios(driver, templist, templist2, S_anio, S_mes)
            driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Casa.aspx')
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='col-xs-12']/p/a")))
        except StaleElementReferenceException:
            pass


def cuales_anios(driver, templist, templist2, S_anio, S_mes):
    #Obtener nombre de la tarifa y minimo mensual de consumo
    nombre_tarifa = driver.find_element(By.CLASS_NAME, 'tituloSubseccion').text
    mm = 25

    #Opciones de años
    select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))

    #Loop por cada una de las opciones de año
    if S_anio == 'TODOS':
        for h in range(0, 3):
            #len(select_year.options)
            #Seleccionar año
            select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
            select_year.select_by_index(h)

            #Obtener nombre del año
            select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
            a = select_year.first_selected_option.text
            scrape(driver, nombre_tarifa, a, mm, templist, templist2, S_mes)
    else:
        # Seleccionar año
        select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
        select_year.select_by_value(S_anio)

        # Obtener nombre del año
        select_year = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_Fecha_ddAnio'))
        a = select_year.first_selected_option.text
        scrape(driver, nombre_tarifa, a, mm, templist, templist2, S_mes)


def scrape(driver, nombre_tarifa, a, mm, templist, templist2, S_mes):
    if nombre_tarifa != "Tarifa 1":
        if nombre_tarifa != "Tarifa DAC":
            mes_de_verano = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_MesVerano1_ddMesVerano'))
            for j in range(2, len(mes_de_verano.options) + 1):
                mes_de_verano = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_MesVerano1_ddMesVerano'))
                mes_de_verano.select_by_value(f'{j}')

                mes_de_verano = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_MesVerano1_ddMesVerano'))
                mdv = mes_de_verano.first_selected_option.text
                id_mes = 'ContentPlaceHolder1_MesVerano2_ddMesConsulta'
                cuales_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, S_mes)
        else:
            mdv = ''
            if driver.find_elements(By.ID, 'ContentPlaceHolder1_Fecha1_ddMes'):
                id_mes = 'ContentPlaceHolder1_Fecha1_ddMes'
            else:
                id_mes = 'ContentPlaceHolder1_MesVerano3_ddMesConsulta'
            cuales_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, S_mes)
    else:
        mdv = ''
        id_mes = 'ContentPlaceHolder1_MesVerano1_ddMesConsulta'
        cuales_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, S_mes)


def cuales_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, S_mes):
    if S_mes == 'TODOS':
        # Opciones de meses
        select_month = Select(driver.find_element(By.ID, id_mes))
        # Loop por cada una de las opciones de meses
        for i in range(1, len(select_month.options)):
            # Seleccionar mes
            select_month = Select(driver.find_element(By.ID, id_mes))
            select_month.select_by_value(f'{i}')

            # Obtener nombre del mes
            select_month = Select(driver.find_element(By.ID, id_mes))
            m = select_month.first_selected_option.text
            loop_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, m)

    else:
        select_month = Select(driver.find_element(By.ID, id_mes))
        select_month.select_by_value(S_mes)

        # Obtener nombre del mes
        select_month = Select(driver.find_element(By.ID, id_mes))
        m = select_month.first_selected_option.text
        loop_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, m)


def loop_meses(driver, nombre_tarifa, a, mdv, mm, templist, id_mes, templist2, m):
    #Ir a la tabla con los precios por kwh
    if driver.find_elements(By.ID, 'ContentPlaceHolder1_TemporadaV'):
        table = driver.find_element(By.ID, 'ContentPlaceHolder1_TemporadaV')
        consumos(table, nombre_tarifa, a, mdv, m, mm, templist)
    elif driver.find_elements(By.ID, 'ContentPlaceHolder1_TemporadaFV'):
        table = driver.find_element(By.ID, 'ContentPlaceHolder1_TemporadaFV')
        consumos(table, nombre_tarifa, a, mdv, m, mm, templist)
    else:
        table = driver.find_element(By.ID, 'TarifaDacFV')
        tarifa_DAC(driver, table, nombre_tarifa, a, m, mm, templist2)
        table = driver.find_element(By.ID, 'TarifaDacV')
        tarifa_DAC(driver, table, nombre_tarifa, a, m, mm, templist2)


def consumos(table, nombre_tarifa, a, mdv, m, mm, templist):
    #Obtener las secciones que tienen los consumos
    rangos = table.find_elements(By.TAG_NAME, 'tr')

    for rango in rangos[2:]:
        #Extraer tipo de consumo, precio y limite de kwh
        x = rango.find_elements(By.TAG_NAME, 'td')
        tl = []

        for y in x:
            #Separar tipo de consumo, precio y limite de kwh, y mandarlos a una lista, quitar los espacios y acentos
            tl.append(y.text.replace('á', 'a').replace(' ', ''))

        #Extraer solo los digitos del limite de kwh
        tl[2] = "".join([ele for ele in tl[2] if ele.isdigit()])

        #Hacer una entrada de diccionario con toda la info
        Table_dict = {
            'Tarifa': nombre_tarifa,
            'Anio': a,
            'Verano': mdv,
            'Mes': m,
            'Consumo': tl[0],
            'Precio': tl[1],
            'kwh': tl[2],
            'Minimo': mm
        }
        #Mandar la entrada a una lista externa
        templist.append(Table_dict)

    #Hacer el file con la info
    df = pd.DataFrame(templist)
    df.to_csv(f'{nombre_tarifa}.csv')


def tarifa_DAC(driver, table, nombre_tarifa, a, m, mm, templist2):
    #Obtener las secciones que tienen los consumos
    rangos = table.find_elements(By.TAG_NAME, 'tr')

    for rango in rangos[2:]:
        #Extraer tipo de consumo, precio y limite de kwh
        x = rango.find_elements(By.TAG_NAME, 'td')
        tl = []

        for y in x:
            #Separar tipo de consumo, precio y limite de kwh, y mandarlos a una lista, quitar los espacios y acentos
            tl.append(y.text.replace('á', 'a').replace(' ', ''))

        if len(tl) == 4:
            #Hacer una entrada de diccionario con toda la info
            Table_dict = {
                'Tarifa': nombre_tarifa,
                'Anio': a,
                'Mes': m,
                'Region': tl[0],
                'Cargo fijo': tl[1],
                'Verano': tl[2],
                'Invierno': tl[3],
                'Minimo': mm
            }
        else:
            Table_dict = {
                'Tarifa': nombre_tarifa,
                'Anio': a,
                'Mes': m,
                'Region': tl[0],
                'Cargo fijo': tl[1],
                'Verano': tl[2],
                'Invierno': '',
                'Minimo': mm
            }
        #Mandar la entrada a una lista externa
        templist2.append(Table_dict)

    #Hacer el file con la info
    df = pd.DataFrame(templist2)
    df.to_csv('DAC.csv')


def NEGOCIO(driver, actions):
    driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Negocio.aspx')

    opciones_tarifas = driver.find_elements(By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]")

    templist = []
    templist2 = []

    for index, val in enumerate(opciones_tarifas):
        try:
            opciones_tarifas = driver.find_elements(By.XPATH, "//div[@id='ContentPlaceHolder1_pnlTarifasCRE']/div[2]")
            actions.move_to_element(opciones_tarifas[index]).perform()
            opciones_tarifas[index].click()
            scrape(driver, templist, templist2)
            driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Casa.aspx')
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='col-xs-12']/p/a")))
        except StaleElementReferenceException:
            pass


CFE()

#app = wx.App(False)
#frame = UI(None)
#frame.Show(True)
##start the applications
#app.MainLoop()