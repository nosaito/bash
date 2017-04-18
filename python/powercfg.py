#!/usr/bin/env python
# -*- coding: utf8 -*-

#import argparse
import os
import os.path
import subprocess

import wx

def main():
    open_gui()
    #get_powercfg_setting()



# 電源設定の GUID: 381b4222-f694-41f0-9685-ff5bb260df2e  (バランス) *
# 電源設定の GUID: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  (高パフォーマンス)
# 電源設定の GUID: a1841308-3541-4fab-bc81-f71556f20b4a  (省電力)

def get_powercfg_setting():
    s = subprocess.check_output( "powercfg /l", shell=True ).decode('sjis')
    #s = subprocess.check_output( "powercfg /l", shell=True )
    #print (s)
    s1 = s.splitlines()

    for s2 in s1:
        if s2.find("電源設定の") > -1 :
            print ( "file: " + s2 )



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

def open_gui():
    wC = {}  # window control dictionary
    application = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(200,150))
    #frame.CreateStatusBar()

    panel = wx.Panel(frame, wx.ID_ANY)
    panel.SetBackgroundColour("#AFAFAF")

    # define control
    wC['button_1'] = wx.Button(panel, wx.ID_ANY, u"ボタン１")
    wC['button_2'] = wx.Button(panel, 3333     , u"ボタン２")
    wC['button_3'] = wx.Button(panel, 4444     , u"ボタン３")

    # set event
    wC['button_1'].Bind(wx.EVT_BUTTON, click_button_1)
    frame.Bind(wx.EVT_BUTTON, click_button, wC['button_2'])
    frame.Bind(wx.EVT_BUTTON, click_button, wC['button_3'])

    # define layout
    layout = wx.BoxSizer(wx.VERTICAL)

    for k in sorted(wC.keys()):
        layout.Add(wC[k], proportion=1, flag=wx.GROW)

    panel.SetSizer(layout)

    frame.Show()
    application.MainLoop()



main()
