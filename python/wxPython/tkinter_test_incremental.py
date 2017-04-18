#!/usr/bin/env python
# -*- coding: utf8 -*-

# case in Python 2.6~
# same print behavior as python 3
from __future__ import print_function

# -*- coding: utf-8 -*-

from tkinter import *

class ListBoxSelector:
    def __init__(self, tkinter_listbox):
        self._lb = tkinter_listbox
        self._update()

    def _update(self):
        selection = self._lb.curselection()
        self._idx = -1
        self._value = ''

        if len(selection)!=0:
            self._idx = int(selection[0])
            self._value = self._lb.get(self._idx)

    def _get_len(self):
        return self._lb.size()

    def _set_idx(self, idx):
        self._lb.selection_clear(0, self._get_len())
        self._lb.selection_set(idx)
        self._lb.see(idx)
        self._update()

    def set_initial_pos(self):
        self._set_idx(-1)

    def down(self):
        new_idx = self._idx + 1
        if new_idx >= self._get_len():
            return
        self._set_idx(new_idx)

    def up(self):
        new_idx = self._idx - 1
        if new_idx < 0:
            return
        self._set_idx(new_idx)

    def get(self):
        self._update()
        return self._idx, self._value

class Application(Frame):
    def __init__(self, root=None):
        self.root=root

        self._on_enter = None
        self._on_text = None

        self._result_selector = None
        self._search_func = self._default_search_func
        self._contents_org = [] # incremental search 用に元リストを保持.

        # 'X' button quitting.
        root.protocol('WM_DELETE_WINDOW', self.quit)

    def _default_focus(self):
        self.querybox.focus()

    def _default_search_func(self, strlist, query):
        if len(query)==0:
            return strlist
        if query[0]==' ':
            return strlist

        ret = []
        for line in strlist:
            if line.find(query)!=-1:
                ret.append(line)
        return ret

    def _default_reflect_func(self):
        items = self._contents_org
        query = self.querybox.get()
        print ('len items:%d' % len(items))

        new_items = self._search_func(items, query)
        self.set_contents(new_items, update_org=False)

        # 検索結果が変わるはずなんでいったんクリア.
        self._result_selector.set_initial_pos()

    # public
    # ------

    def create(self):
        Frame.__init__(self, root)
        self.pack()

        # widget support
        # --------------
        self.querybox_sv = StringVar()
        def on_text(name, index, mode, sv=self.querybox_sv):
            text = sv.get()
            self._on_text(text)
            self._default_reflect_func()
        self.querybox_sv.trace('w', on_text)

        # widget def
        # ----------
        self.querybox = Entry(master=self.root, textvariable=self.querybox_sv)
        self.searchresult = Listbox(master=self.root,
                                    exportselection=0)
        self.yscroll = Scrollbar(master=self.root, orient=VERTICAL)

        # packing
        # -------
        self.querybox.pack({'side':'top', 'fill':'x'})
        self.yscroll.pack({'side':'right', 'fill':'y'})
        self.searchresult.pack({'side':'top', 'fill':'x'})

        # listbox
        # -------
        # scrollbar relationship
        self.yscroll.config(command=self.searchresult.yview)
        self.searchresult.config(yscrollcommand=self.yscroll.set)
        # status controller relationship
        self._result_selector = ListBoxSelector(self.searchresult)

        # binds
        # -----
        def on_enter(ev):
            idx, value = self._result_selector.get()
            self._on_enter(idx, value)

        def on_key(ev):
            k = ev.keycode
            if k==38: # up=38
                self._result_selector.up()
                return 'break'
            if k==40: # down=40
                self._result_selector.down()
                return 'break'

        def selectall(ev):
            self.querybox.select_range(0, END)
            return 'break'

        def do_nothing(*args, **kwargs):
            return 'break'

        self.querybox.bind('<Return>', on_enter)
        self.querybox.bind('<Control-a>', selectall)
        self.querybox.bind('<Control-d>', do_nothing)
        self.querybox.bind('<Control-/>', do_nothing)
        self.querybox.bind('<KeyPress>', on_key)

        # rest preperation
        # ----------------
        self._default_focus()

    def set_on_enter(self, on_enter):
        """ on_enter(idx, value) """
        self._on_enter = on_enter

    def set_on_text(self, on_text):
        """ on_text(new_string) """
        self._on_text = on_text

    def set_contents(self, contents, update_org=True):
        """ @param contens A string list.
        Must be called after create(). """
        if update_org:
            import copy
            self._contents_org = copy.deepcopy(contents)

        sr = self.searchresult
        size = sr.size()
        sr.delete(0, size)

        for elm in contents:
            sr.insert(END, elm)

root = Tk()
root.title('いんくりめんたるさーち')
root.geometry('320x100+0+0')

app = Application(root=root)
def on_text(new_stirng):
    print ('changed!: new=[%s]' % new_stirng)
app.set_on_text(on_text)
def on_enter(idx, value):
    print ('%d, %s' % (idx, value))
app.set_on_enter(on_enter)
app.create()
app.set_contents(['data%d'%elm for elm in range(32)])

app.mainloop()
root.destroy()
