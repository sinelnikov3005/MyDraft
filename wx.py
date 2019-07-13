import wx


class Window(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 250))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)  # создаём текстовое поле
        self.Show(True)

        menu = wx.Menu()  # создаём экземпляр меню
        menu.Append(wx.ID_ABOUT, "About",
                    "Push the button to get an information about this application")  # добавляем подпункты к меню
        menu.Append(wx.ID_EXIT, "Exit", "Push the button to leave this application")  # а как ещё?
        bar = wx.MenuBar()  # создаём рабочую область для меню
        bar.Append(menu, "File")  # добавляем пункт меню
        self.SetMenuBar(bar)  # указываем, что это меню надо показать в нашей форме


app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()
