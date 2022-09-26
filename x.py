import wx

class Mywin(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(300, 400))
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Your choice:", style=wx.ALIGN_CENTRE)
        box.Add(self.label, 0, wx.EXPAND | wx.ALL, 20)

        cbo1 = wx.StaticText(panel, label="Tipo", style=wx.ALIGN_CENTRE)
        box.Add(cbo1, 0, wx.EXPAND | wx.ALL, 5)

        tipos = ['Residencial', 'Comercial', 'Todas']
        tarifas = ['1', '1A', '1B', '1C', '1D', '1E', '1F', 'Todas']
        anios = ['2022', '2021', '2020', '2019', 'Todos']
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Todos']

        self.cb1 = wx.ComboBox(panel, choices=tipos)
        box.Add(self.cb1, 1, wx.EXPAND | wx.ALL, 5)

        box.AddStretchSpacer()
        cbo2 = wx.StaticText(panel, label="Tarifa", style=wx.ALIGN_CENTRE)
        box.Add(cbo2, 0, wx.EXPAND | wx.ALL, 5)

        self.cb2 = wx.ComboBox(panel, choices=tarifas)
        box.Add(self.cb2, 1, wx.EXPAND | wx.ALL, 5)

        box.AddStretchSpacer()
        cbo3 = wx.StaticText(panel, label="Año", style=wx.ALIGN_CENTRE)
        box.Add(cbo3, 0, wx.EXPAND | wx.ALL, 5)

        self.cb3 = wx.ComboBox(panel, choices=anios)
        box.Add(self.cb3, 1, wx.EXPAND | wx.ALL, 5)

        box.AddStretchSpacer()
        cbo4 = wx.StaticText(panel, label="Mes", style=wx.ALIGN_CENTRE)
        box.Add(cbo4, 0, wx.EXPAND | wx.ALL, 5)

        self.cb4 = wx.ComboBox(panel, choices=meses)
        box.Add(self.cb4, 1, wx.EXPAND | wx.ALL, 5)

        box.AddStretchSpacer()

        self.cb1.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        panel.SetSizer(box)
        self.Centre()
        self.Show()

    #----------------------------------------------------------------------
    def OnCombo(self, event):
        self.label.SetLabel("selected " + self.cb1.GetValue() + " from Combobox")

# Run the program

app = wx.App()
Mywin(None, 'ComboBox and Choice demo')
app.MainLoop()