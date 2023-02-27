import wx
import wx.grid as gridlib

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Address finder', size=(400,200))
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.panel = wx.Panel(self)        
        self.my_sizer = wx.BoxSizer(wx.VERTICAL)   
        self.lblname = wx.StaticText(self.panel, label="Your address (hexa) 0x")  
        self.my_sizer.Add(self.lblname, 0, wx.ALL | wx.CENTER, 0)     
        self.text_ctrl = wx.TextCtrl(self.panel)
        self.my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 0)        
        my_btn = wx.Button(self.panel, label='Update')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5) 

        self.grid = gridlib.Grid(self.panel)
        self.grid.CreateGrid(2, 3)
        self.grid.SetColLabelValue(0, "bin")
        self.grid.SetColLabelValue(1, "hex")
        self.grid.SetColLabelValue(2, "dec")
        self.grid.SetRowLabelValue(0, "index")
        self.grid.SetRowLabelValue(1, "tag")
        self.grid.SetDefaultCellFont(font)
        self.grid.SetColSize(0,100)
        self.my_sizer.Add(self.grid, 0, wx.ALL | wx.CENTER, 0)  
 
        self.panel.SetSizer(self.my_sizer)        
        self.Show()

    def on_press(self, event):
        self.value = self.text_ctrl.GetValue()
        if not self.value:
            print("You didn't enter anything!")
        else:
            self.strhex2int()
            print(f'value :{self.value}')
            addr_bin = bin(int(self.value))
            index = (int(self.value)>>4) % pow(2,4)
            tag = int(self.value)>>8

            self.grid.SetCellValue(0, 0, str(bin(index)))
            self.grid.SetCellValue(0, 1, str(hex(index)))
            self.grid.SetCellValue(0, 2, str(index))
            self.grid.SetCellValue(1, 0, str(bin(tag)))
            self.grid.SetCellValue(1, 1, str(hex(tag)))
            self.grid.SetCellValue(1, 2, str(tag))
            self.grid.AutoSizeColumns(1)
            # print(f'e"{hex(value)}"')
            # print(f'You typed: "{bin(int(hex(value)))}"')

    def strhex2int(self):
        inter = 0
        numberr = 0

        checkWords   = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" )
        replaceWords = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15")
        for carac in reversed(self.value) :   
            for check, rep in zip(checkWords, replaceWords):
                carac = carac.replace(check, rep)
            inter += int(carac)*pow(16,int(numberr))
            # print(f'carac :{carac}')
            # print(f'i     :{numberr}')
            # print(f'inter :{inter}')
            # print(f'puis  :{pow(16,int(numberr))}')
            # print("")
            numberr += 1
        #print(self.value[0])
        self.value=inter
        
    


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

