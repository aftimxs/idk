import wx

import cfeui


class CalcFrame(cfeui.MyFrame1):
    def __init__(self, parent):
        cfeui.MyFrame1.__init__(self, parent)


app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()