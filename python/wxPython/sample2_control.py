#!/usr/bin/env python
# -*- coding: utf8 -*-


# http://labs.beatcraft.com/ja/index.php?Python%2FwxPython%A4%CB%A4%E8%A4%EBWindowsGUI%A5%D7%A5%ED%A5%B0%A5%E9%A5%DF%A5%F3%A5%B0

import wx

class SampleApp(wx.App):
    def OnInit(self):
        self.init_frame()
        return True

    def init_frame(self):
        self.frm_main = wx.Frame(None)

        # place Sizer
        self.sizer = wx.BoxSizer()
        self.frm_main.SetSizer(self.sizer)

        # place TextCtrl
        self.txt_title = wx.TextCtrl(self.frm_main)
        self.sizer.Add(self.txt_title, 1, wx.ALIGN_CENTER_VERTICAL)

        # place Button
        self.btn_submit = wx.Button(self.frm_main)
        self.btn_submit.SetLabel("Change Title")
        self.btn_submit.Bind(wx.EVT_BUTTON, self.on_submit)
        self.sizer.Add(self.btn_submit, 0, wx.ALIGN_CENTER_VERTICAL)

        # set window property
        self.frm_main.SetTitle("sample_2_3")
        self.frm_main.SetSize((400, 200))
        self.frm_main.Show()

    def on_submit(self, event):
        self.frm_main.SetTitle(self.txt_title.GetValue())
        self.txt_title.SetValue("")

if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()
