#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""


**************************
文件:     wxpython
 IDE：    PyCharm
创建时间： 2019/6/15 18:08
@author： skymoon
"""

import wx


# 展示窗口
class MyApp(wx.App):

    def OnInit(self):
        frame = wx.Frame(None, title="Hello, World!")
        frame.Show(True)
        return True


# 文本显示
class Text(wx.Frame):

    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title="Example", pos=(100, 200), size=(200, 100))
        self.panel = wx.Panel(self)
        text = wx.TextCtrl(self.panel, value="Hello, World!", size=(200, 100))


# 点击位置添加文本
class OnClickText(wx.Frame):

    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title="Example", pos=(100, 200), size=(200, 100))
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnClick)

    def OnClick(self, event):
        posm = event.GetPosition()
        wx.StaticText(parent=self.panel, label="Hello, World!", pos=(posm.x, posm.y))


# 点击按钮添加文本
class ButtonClickText(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title="Hello World in wxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, value="Hello, World!", size=(200, 180), style=wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)

    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")


if __name__ == "__main__":
    app = wx.App()
    # frame = Text(None)
    # frame.Show(True)
    # frame2 = OnClickText(None)
    # frame2.Show(True)
    frame3 = ButtonClickText(None)
    frame3.Show(True)
    app.MainLoop()
