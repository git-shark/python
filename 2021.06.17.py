# wx.Pythonのインストール
# pip install -U wxPython

def Main():
    PieceSize = 20
    BoardWidth = 10
    BoardHeight = 22
    PanelWidth = PieceSize * BoardWidth
    PanelHeight = PieceSize * BoardHeight

    frame = wx.Frame(None, title = 'TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    frame.Center()
    frame.Show()

if __name__ == "__main__":
    import wx
    app = wx.App()
    Main()
    app.MainLoop()