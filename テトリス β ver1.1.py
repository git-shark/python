# pythonはプログラムを走らせると変数__name__に文字列'__main__'を自動的に代入する
# プログラムが直接起動した場合の判定、コマンドラインやファイルからの起動時にTrueとなる
# __main__、すなわちファイルやコマンドラインから直接起動したよ。の意味
# 他のプログラムから呼ばれた場合は、そのプログラム名が代入される

# イベント発生により処理をさせる = イベントドリブン
# その処理を担当するプログラム = イベントハンドラ(コールバック関数)

# board 0-9 or 0-21
# PieceSize = サイズは20、描写は0-19の値をとる
# y+(piecesize-1)=19を示す piecesizeは0-19で描写されている

def SetBlockOnBoard(set_board, block_coords, x, y, block_shape):
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        set_board[piece_y][piece_x] = block_shape

def DrawBlock(copy_board, block_coords, x, y, block_shape):
    global board
    global curBlockCoords, curShape, curX, curY

    SetBlockOnBoard(copy_board, block_coords, x, y, block_shape)
    board = copy.deepcopy(copy_board)
    curBlockCoords = copy.deepcopy(block_coords)
    [curShape, curX, curY] = [block_shape, x, y]
    panel.Refresh()                    #前データを削除し再描画  ※再描写後「描写メッセージ(EVT_PAINT)が発生」

def CheckMoveAvailable(check_board, block_coords, x, y):
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        if piece_x < 0 or piece_x > BoardWidth - 1 or\
            piece_y < 0 or piece_y > BoardHeight - 3 or\
                check_board[piece_y][piece_x] != 0:
            return False
        return True

def OnKeyDown(event):
    global isCurBlock, isKeyDown

    if keyAllowed is False or isKeyDown is True:
        return

    isKeyDown = True

    keycode = event.GetKeyCode()
    if keycode == wx.WXK_LEFT or keycode == wx.WXK_RIGHT:
        copy_board = copy.deepcopy(board)
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)
        nextBlockCoords = copy.deepcopy(curBlockCoords)
        [nextX, nextY] = [curX, curY]

        if keycode == wx.WXK_LEFT:
            nextX = curX - 1
        elif keycode == wx.WXK_RIGHT:
            nextX = curX + 1

        if CheckMoveAvailable(copy_board, nextBlockCoords, nextX, nextY):
            DrawBlock(copy_board, nextBlockCoords, nextX, nextY, curShape)
            isCurBlock = True
    isKeyDown = False

def OnTimer(event):                    #event=panel、慣例で仮引数には(event)表記を用いる
    global isCurBlock, keyAllowed      #フラグ(描写判定用)グローバル化

    if event.GetId() != ID_TIMER or isKeyDown is True:      #イベント発生源がpanelか否かの判定
        return

    keyAllowed = False
    copy_board = copy.deepcopy(board)
    if not isCurBlock:
        newShape = random.randint(1, 7)
        newBlockCoords = copy.deepcopy(BlockTable[newShape])
        [newX, newY] = [int(BoardWidth / 2), 1]
        if not CheckMoveAvailable(copy_board, newBlockCoords, newX, newY):
            event.GetTimer().Stop()
            return
        else:
            DrawBlock(copy_board, newBlockCoords, newX, newY, newShape)
            isCurBlock = True
    else:
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)
        if not CheckMoveAvailable(copy_board, curBlockCoords, curX, curY + 1):
            isCurBlock = False
        else:
            DrawBlock(copy_board, curBlockCoords, curX, curY + 1, curShape)
    keyAllowed = True

def OnPaint(event):
    obj = event.GetEventObject()               #obj = <wx._core.Panel object at 0x0000022D73074AF0> がBoardHeight分処理
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
    global BlockTable
    global isCurBlock, keyAllowed, isKeyDown
    global panel
    global ID_TIMER, timer

    [PieceSize, BoardWidth, BoardHeight] = [20, 10, 22]
    PanelWidth = PieceSize * BoardWidth
    PanelHeight = PieceSize * BoardHeight
    ShapeNo = [[0, 0], [0, 0], [0, 0], [0, 0]]
    ShapeZ = [[0, -1], [0, 0], [-1, 0], [-1, 1]]
    ShapeS = [[0, -1], [0, 0], [1, 0], [1, 1]]
    ShapeLine = [[0, -1], [0, 0], [0, 1], [0, 2]]
    ShapeT = [[-1, 0], [0, 0], [1, 0], [0, 1]]
    ShapeSquare = [[0, 0], [1, 0], [0, 1], [1, 1]]
    ShapeL = [[-1, -1], [0, -1], [0, 0], [0, 1]]
    ShapeMirroredL = [[1, -1], [0, -1], [0, 0], [0, 1]]
    BlockTable = [ShapeNo, ShapeZ, ShapeS, ShapeLine, ShapeT, ShapeSquare, ShapeL, ShapeMirroredL]

    colors = ['BLACK', wx.Colour('RED'), wx.Colour('GREEN'), wx.Colour('BLUE'), wx.Colour('YELLOW'),\
        wx.Colour('CYAN'), wx.Colour('LIGHT BLUE'), wx.Colour('VIOLET RED')]
    light = ['BLACK']
    dark = ['BLACK']
    for i in range(1, 8):
        light.append(colors[i].ChangeLightness(150)) #['BLACK', wx.Colour(255, 127, 127, 255), wx.Colo・・・・
        dark.append(colors[i].ChangeLightness(50))

    board = []
    for i in range(BoardHeight):
        board_row = [0] * BoardWidth
        board.append(board_row)
    [isCurBlock, keyAllowed, isKeyDown] = [False] * 3

    frame = wx.Frame(None, title = 'TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    panel.Bind(wx.EVT_PAINT, OnPaint)                 #panel.Refresh()実行 => (EVT_PAINT)が発生 => OnPaint関数へ
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)
    ID_TIMER = 1
    timer = wx.Timer(panel, ID_TIMER)                 #panelのIDを1としている
    panel.Bind(wx.EVT_TIMER, OnTimer, id = ID_TIMER)                 #タイマーイベント発生毎に、コールバック関数OnTimeを実行
    Speed = 100                                       #ミリ秒
    timer.Start(Speed)                                #100ms毎にイベント(EVT_TIMER)発生
    panel.Bind(wx.EVT_CHAR_HOOK, OnKeyDown)
    frame.Center()
    frame.Show()

if __name__ == "__main__":
    import wx
    import copy
    import random
    app = wx.App()
    Main()
    app.MainLoop()