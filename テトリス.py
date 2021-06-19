# pythonはプログラムを走らせると変数__name__に文字列'__main__'を自動的に代入する
# プログラムが直接起動した場合の判定、コマンドラインやファイルからの起動時にTrueとなる
# __main__、すなわちファイルやコマンドラインから直接起動したよ。の意味
# 他のプログラムから呼ばれた場合は、そのプログラム名が代入される

# イベント発生により処理をさせる = イベントドリブン
# その処理を担当するプログラム = イベントハンドラ(コールバック関数)

def OnPaint(event):
    obj = event.GetEventObject()
    dc = wx.BufferedPaintDC(obj)
    dc.Clear()

    for i in range(BoardHeight):
        for j in range(BoardWidth):
            shape = board[i][j]
            if shape != 0:
                [x, y] = [j * PieceSize, i * PieceSize]

                lightpen = wx.Pen(light[shape])
                lightpen.SetCap(wx.CAP_PROJECTING)
                dc.SetPen(lightpen)
                dc.DrawLine(x, y, x, y + PieceSize - 1)
                dc.DrawLine(x, y, x + PieceSize - 1, y)

                darkpen = wx.Pen(dark[shape])
                darkpen.SetCap(wx.CAP_PROJECTING)
                dc.SetPen(darkpen)
                dc.DrawLine(x + 1, y + PieceSize - 1, x + PieceSize - 1, y + PieceSize - 1)
                dc.DrawLine(x + PieceSize - 1, y + 1, x + PieceSize - 1, y + PieceSize - 1)

                dc.SetPen(wx.TRANSPARENT_PEN)
                dc.SetBrush(wx.Brush(colors[shape]))
                dc.DrawRectangle(x + 1, y + 1, PieceSize - 2, PieceSize -2)

def OnEraseBackground(event):
    pass

def Main():
    global PieceSize
    global BoardWidth, BoardHeight
    global PanelWidth, PanelWidth
    global colors, light, dark
    global board

    [PieceSize, BoardWidth, BoardHeight] = [20, 10, 22]
    PanelWidth = PieceSize * BoardWidth
    PanelHeight = PieceSize * BoardHeight

    colors = ['BLACK', wx.Colour('RED')]
    light = ['BLACK', colors[1].ChangeLightness(150)]
    dark = ['BLACK', colors[1].ChangeLightness(50)]

    board = []
    for i in range(BoardHeight):
        board_row = [0] * BoardWidth
        board.append(board_row)

    frame = wx.Frame(None, title = 'TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    panel.Bind(wx.EVT_PAINT, OnPaint)
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)
    frame.Center()
    frame.Show()

if __name__ == "__main__":
    import wx
    app = wx.App()
    Main()
    board[4][5] = 1
    app.MainLoop()