
import wx

class ImagePanel(wx.Panel):
    def __init__(self,parent, image_size):
        super().__init__(parent)
        img = wx.Imagge(*image_size)
        self.image_ctrl = wx.StaticBitmap(self,bitmap=wx.Bitmap(img))
        browse_btn = wx.Button(self, label="Procurar")

        main_sizer = wx.BoxSizer(wx.Vertical)
        main_sizer.Add(self.image_ctrl,0,wx.all,5)
        main_sizer.Add(browse_btn)
        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()

        