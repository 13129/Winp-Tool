# -*- coding: utf-8 -*-
# 作者：LeniyTsan
# 时间：2014-07-17

import wx
from wx.lib.embeddedimage import PyEmbeddedImage
import img

class MyFrame1 (wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        # file = open('author.png', 'rb')
        b64 = img.intel_net
        # file.close()
        bitmap = PyEmbeddedImage(b64).GetBitmap()
        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
        bSizer1.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)
        self.Centre(wx.BOTH)
app = wx.App()
gui = MyFrame1(None)
gui.Show()
app.MainLoop()
