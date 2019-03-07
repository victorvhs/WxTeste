
import wx

class ImagePanel(wx.Panel):
    def __init__(self,parent, image_size):
        super().__init__(parent)
        self.max_size = 280
        img = wx.Image(*image_size)
        self.image_ctrl = wx.StaticBitmap(self,bitmap=wx.Bitmap(img))
        # eventos
        browse_btn = wx.Button(self, label="Procurar")
        browse_btn.Bind(wx.EVT_BUTTON, self.on_Browse)

        self.photo_txt = wx.TextCtrl(self,size=(200,-1))
        # Cria o layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        #Adiciona os elementos ao layout
        main_sizer.Add(self.image_ctrl,0,wx.ALL,5)
        hsizer.Add(browse_btn,0,wx.ALL,5)
        hsizer.Add(self.photo_txt,0,wx.ALL,5)
        main_sizer.Add(hsizer,0,wx.ALL,5)
        
        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()
    def on_Browse(self,event):
        """
        Procura o arquivo de imagem
        @param event: O evento do objeto
        """
        wildcard = "JPEG files(*.jpg)|*.jpg"
        with wx.FileDialog(None, "Escolha o Arquivo", wildcard=wildcard, style=wx.ID_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_txt.SetValue(dialog.GetPath())
                self.load_image()
    
    def load_image(self):
        """
        Carrega a imagem
        """
        filepath = self.photo_txt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # redimensionar a imagem, sem perder o aspecto
        W = img.GetWidth()
        H = img.GetHeight()

        if W >H:
            NewW = self.max_size
            NewH = self.max_size * H/w
        else:
            NewH = self.max_size
            NewW = self.max_size * W/H
        img = img.Scale(NewW,NewH)

        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Image Viewer")
        panel = ImagePanel(self,image_size=(280,280))
        self.Show()

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()