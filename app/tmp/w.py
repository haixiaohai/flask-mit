import wx
import wx.adv 
   

class MitTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = 'logo.ico'
    ID_ABOUT = wx.NewIdRef()
    ID_EXIT = wx.NewIdRef()
    ID_SHOW_WEB = wx.NewIdRef()
    TITLE = 'Maipu Inspection Tools'

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON),self.TITLE)
        self.Bind(wx.EVT_MENU,self.onAbout,id=self.ID_ABOUT)
        self.Bind(wx.EVT_MENU,self.onExit,id=self.ID_EXIT)
        self.Bind(wx.EVT_MENU,self.onShowWeb,id=self.ID_SHOW_WEB)

    def onAbout(self,event):
        wx.MessageBox('006007')

    def onExit(self,event):
        wx.Exit()

    def onShowWeb(self,event):
        pass

    def createicon(self):
        menu = wx.Menu()
        for mentattr in self.getmenuattrs():
            menu.Append(mentattr[1],mentattr[0])

        return menu

    def getmenuattrs(self):
        return [('打开页面',self.ID_SHOW_WEB),
                ('关于',self.ID_ABOUT),
                ('退出',self.ID_EXIT)]


class MitFrame(wx.Frame):

    def __init__(self,*args,**kwargs):
        super(MitFrame,self).__init__(*args,**kwargs)
        
        wx.Frame.__init__(self)
        MitTaskBarIcon()


class MitApp(wx.App):
    def onInit(self):
        MitFrame()
        return True


if __name__ == '__main__':
    guiapp = wx.App()
    frm = wx.Frame(None,title='Maipu Inspection Tools')
    frm.Show()
    guiapp.MainLoop()