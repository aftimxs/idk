import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,197 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"CFE", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )

        tipos = ['Residencial', 'Comercial', 'Todas']
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Tipos", wx.DefaultPosition, wx.DefaultSize, tipos, wx.CB_DROPDOWN )
        bSizer1.Add( self.m_comboBox1, 0, wx.ALL|wx.EXPAND, 5 )

        tarifas = ['1', '1A', '1B', '1C', '1D', '1E', '1F', 'Todas']
        self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Tarifa", wx.DefaultPosition, wx.DefaultSize, tarifas, wx.CB_DROPDOWN )
        bSizer1.Add( self.m_comboBox2, 0, wx.ALL|wx.EXPAND, 5 )

        anios = ['2022', '2021', '2020', '2019', 'Todos']
        self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Año", wx.DefaultPosition, wx.DefaultSize, anios, wx.CB_DROPDOWN )
        bSizer1.Add( self.m_comboBox3, 0, wx.ALL|wx.EXPAND, 5 )

        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                 'Noviembre', 'Diciembre', 'Todos']
        self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Mes", wx.DefaultPosition, wx.DefaultSize, meses, wx.CB_DROPDOWN )
        bSizer1.Add( self.m_comboBox4, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


    #Ir a la pagina principal de la CFE
    #driver.get('https://www.cfe.mx/Pages/default.aspx')

    #Click en "Servicios"
    #servicios = driver.find_element(By.LINK_TEXT, "SERVICIOS")
    #actions.move_to_element(servicios).perform()
    #servicios.click()
#
    #op_serv = []
#
    ##Obtener opciones dentro de "Servicios"
    #opciones_servicios = driver.find_elements(By.XPATH, "//nav[@id='primary-menu']/ul/li[2]/div/ul")

# for x, y in enumerate(opciones_servicios):
#    op_serv.append(y)
#
##Loopear por cada opcion
# for index, val in enumerate(op_serv):
#    try:
#        print(val.text)
#        #Click en cada opcion
#        z = driver.find_elements(By.LINK_TEXT, val.text)
#        actions.move_to_element(z[index]).perform()
#        z[index].click()
#
#        # LLamar funcion de scrape de tarifas residenciales
#        for key, y in funciones.items():
#            if key == val.text:
#                y(driver, actions)
#            else:
#                pass
#
#        #Regresar a la pagina principal
#        time.sleep(2)
#        driver.get('https://www.cfe.mx/Pages/default.aspx')
#        time.sleep(2)
#        WebDriverWait(driver, 20).until(
#            EC.visibility_of_element_located((By.LINK_TEXT, "SERVICIOS")))
#        servicios = driver.find_element(By.LINK_TEXT, "SERVICIOS")
#        actions.move_to_element(servicios).perform()
#        servicios.click()
#        time.sleep(2)
#
#    except StaleElementReferenceException:
#        pass

    # Click en "Tarifas"
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #    (By.XPATH, "//div[@id='ctl00_PlaceHolderMain_g_29e5d067_04c6_4ad8_813d_1e8fcfb17946']/div[3]")))
    #dropdown = driver.find_element(By.XPATH,
    #                               "//div[@id='ctl00_PlaceHolderMain_g_29e5d067_04c6_4ad8_813d_1e8fcfb17946']/div[3]")
    #actions.move_to_element(dropdown).perform()
    #dropdown.click()

    # Click en "Esquema tarifario vigente"
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Esquema tarifario vigente")))
    #tarifas_dropdown = driver.find_element(By.LINK_TEXT, "Esquema tarifario vigente")
    #actions.move_to_element(tarifas_dropdown).perform()
    #tarifas_dropdown.click()


    # Click en "Tarifas"
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #    (By.XPATH, "//div[@id='ctl00_PlaceHolderMain_g_29e5d067_04c6_4ad8_813d_1e8fcfb17946']/div[3]")))
    #dropdown = driver.find_element(By.XPATH,
    #                               "//div[@id='ctl00_PlaceHolderMain_g_29e5d067_04c6_4ad8_813d_1e8fcfb17946']/div[3]")
    #actions.move_to_element(dropdown).perform()
    #dropdown.click()

    ## Click en "Esquema tarifario vigente"
    #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Esquema tarifario vigente")))
    #tarifas_dropdown = driver.find_element(By.LINK_TEXT, "Esquema tarifario vigente")
    #actions.move_to_element(tarifas_dropdown).perform()
    #tarifas_dropdown.click()
