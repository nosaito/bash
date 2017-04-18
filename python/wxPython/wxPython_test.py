#!/usr/bin/env python
# -*- coding: utf8 -*-

#
# wxPython :
#   http://www.python-izm.com/contents/gui/wxpython.shtml
#


import wx

def click_button_1(event):
    frame.SetStatusText("Click! button_1")
    print("button 1 is pressed.")

def click_button_2(event):
    frame.SetStatusText("Click! button_2")

def click_button(event):
    if event.GetId() == 3333:
        frame.SetStatusText("Click! button_2")
    elif event.GetId() == 4444:
        frame.SetStatusText("Click! button_3")

def selectMenu(event):
    frame.SetStatusText("MenuSelected! " + str(event.GetId()))



wC = {}  # window control dictionary
application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(400,700))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

# add Menu
menu_file = wx.Menu()
menu_file.Append(1, u"保存")
menu_file.Append(2, u"終了")
menu_edit = wx.Menu()
menu_edit.Append(3, u"コピー")
menu_edit.Append(4, u"貼り付け")
menu_bar = wx.MenuBar()
menu_bar.Append(menu_file, u"ファイル")
menu_bar.Append(menu_edit, u"編集")
frame.SetMenuBar(menu_bar)
frame.Bind(wx.EVT_MENU,selectMenu)  # Bind(event type, function



# define control
wC['button_1'] = wx.Button(panel, wx.ID_ANY, u"ボタン１")
wC['button_2'] = wx.Button(panel, 3333     , u"ボタン２")
wC['button_3'] = wx.Button(panel, 4444     , u"ボタン３")
wC['s_text_1'] = wx.StaticText(panel, wx.ID_ANY, u"テキスト１")
wC['text_1'] = wx.TextCtrl(panel, wx.ID_ANY, u"初期値")
wC['ckbox_1'] = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス１")
wC['rbtn_1'] = wx.RadioButton(panel, wx.ID_ANY, u"ラジオボタン１")
wC['rbtn_2'] = wx.RadioButton(panel, wx.ID_ANY, u"ラジオボタン2")
button_array = ("RB1", "RB2", "RB3", "RB4")
wC['rbox_1'] = wx.RadioBox(panel, wx.ID_ANY, "python-izm.com", choices=button_array, style=wx.RA_VERTICAL)
element_array = ("element_1", "element_2", "element_4", "element_3", "element_5")
wC['comboBox_1']  = wx.ComboBox(panel, wx.ID_ANY, u"選択してください", choices=element_array, style=wx.CB_SIMPLE)


# set event
wC['button_1'].Bind(wx.EVT_BUTTON, click_button_1)
frame.Bind(wx.EVT_BUTTON, click_button, wC['button_2'])
frame.Bind(wx.EVT_BUTTON, click_button, wC['button_3'])

# define layout
layout = wx.BoxSizer(wx.VERTICAL)
#layout.Add(wC['button_1'], proportion=1)
#layout.Add(wC['button_2'], proportion=1)
#layout.Add(wC['button_3'], proportion=1)

for k in sorted(wC.keys()):
    layout.Add(wC[k], proportion=1, flag=wx.GROW)


panel.SetSizer(layout)

frame.Show()
application.MainLoop()
