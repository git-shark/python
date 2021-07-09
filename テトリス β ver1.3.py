# -*- coding: utf-8 -*-

#board上にshape番号を記載
def SetBlockOnBoard(set_board, block_coords, x, y, block_shape): #self挿入
    for i in range(-1,3):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        set_board[piece_y][piece_x] = block_shape
        print('x:', piece_x, 'y:', piece_y)
        #print(isCurBlock)

#block描写
def DrawBlock(copy_board, block_coords, x, y, block_shape):      #Draw  描く
    global board
    global curBlockCoords,curShape, curX, curY                   #Cur = カー  雑種

    SetBlockOnBoard(copy_board, block_coords, x, y, block_shape) #初期boardがSetBlockOnBoardされてくる
    board = copy.deepcopy(copy_board)                            #SetBlockOnBoardされた値をboardに代入
    curBlockCoords = copy.deepcopy(block_coords)
    [curShape, curX, curY] = [block_shape, x, y]
    panel.Refresh()                                              #ここで描写 + EVT_信号を発生

#領域を判定
def CheckMoveAvailable(check_board, block_coords, x, y):         #flag判定   アベイラブル = 利用できる、空いている
    for i in range(-1,3):
        piece_x = block_coords[i][0] + x                            #coords = コーズ  領域  座標
        piece_y = block_coords[i][1] + y
        if piece_x < 0 or piece_x > BoardWidth - 1 or piece_y < 0 or piece_y > BoardHeight - 1 or check_board[piece_y][piece_x] != 0:
            print(False)
            return False

    print(True)
    return True

#block種選定 → 判定 → block落下
def OnTimer(event):
    global isCurBlock

    if event.GetId() != ID_TIMER:
        return

    copy_board = copy.deepcopy(board)

    if not isCurBlock:
        newShape = random.randint(1, 7)
        newBlockCoords = copy.deepcopy(BlockTable[newShape])
        [newX, newY] = [int(BoardWidth / 2), 1]

        if not CheckMoveAvailable(copy_board, newBlockCoords, newX, newY):
            print("flag=False + Check=False, 停止")
            event.GetTimer().Stop()
            return
        else:
            DrawBlock(copy_board, newBlockCoords, newX, newY, newShape)
            print("flag=False + Check=True")
            isCurBlock = True
            return
    else:
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)              #前の描写を削除

        if not CheckMoveAvailable(copy_board, curBlockCoords, curX, curY + 1):  #次に描写する領域チェック 4に変更
            print("flag=True + Check=False")
            isCurBlock = False
            return
        else:
            DrawBlock(copy_board, curBlockCoords, curX, curY + 1, curShape)     #ブロックを一マス落下
            print("flag=True + Check=True, 描写")
            return

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
                dc.DrawLine(x, y, x, y + PieceSize -  1)
                dc.DrawLine(x, y, x + PieceSize - 1, y)

                darkpen = wx.Pen(dark[shape])
                darkpen.SetCap(wx.CAP_PROJECTING)
                dc.DrawLine(x + 1, y + PieceSize - 1, x + PieceSize - 1, y + PieceSize - 1)
                dc.DrawLine(x + PieceSize - 1, y + 1, x + PieceSize - 1, y + PieceSize - 1)

                dc.SetPen(wx.TRANSPARENT_PEN)
                dc.SetBrush(wx.Brush(colors[shape]))
                dc.DrawRectangle(x + 1, y + 1, PieceSize - 2, PieceSize - 2)

def OnEraseBackground(event):
    pass

def Main():
    global PieceSize
    global BoardWidth, BoardHeight
    global PanelWidth, PanelHeight
    global colors, light, dark
    global board
    global BlockTable
    global isCurBlock
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

    BlockTable = [ShapeNo, ShapeZ, ShapeS, ShapeLine, ShapeT,\
        ShapeSquare, ShapeL, ShapeMirroredL]

    colors = ['BLACK', wx.Colour('RED'), wx.Colour('GREEN'),\
        wx.Colour('BLUE'), wx.Colour('YELLOW'), wx.Colour('CYAN'),\
        wx.Colour('LIGHT BLUE'), wx.Colour('VIOLET RED')]

    light = ['BLACK']
    dark = ['BLACk']
    for i in range(1, 8):
        light.append(colors[i].ChangeLightness(150))
        dark.append(colors[i].ChangeLightness(50))

    board = []
    for i in range(BoardHeight):
        board_row = [0] * BoardWidth
        board.append(board_row)

    isCurBlock = False                        #再描写の有無判定用フラグ  ※初期値=False

    frame = wx.Frame(None, title='TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)                   #インスタンス作成
    panel.SetBackgroundColour('BLACK')        #panel objへの描写 → OSが描写信号を出力
    panel.Bind(wx.EVT_PAINT, OnPaint)         #wx.EVT_PAINTが描写信号を捕捉しpanel objを出力 → OnPaint(paint obj)で呼び出し
                                              #OSが発した描写信号を得て処理 → イベントドリブン  ※wxPythonはこの手法で駆動
                                              #この場合、OSがpanelに生じた描写を信号出力しEVTで捕捉しOnPaintに処理を委ねる
                                              #wx.EVT_PAINT = <wx.core.PyEventBinder object at 0x00000264E800CF88>
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)   #<wx.core.PyEventBinder object at 0x00000264E800E048>
    ID_TIMER = 1                              #timer固有識別子=1  ※タイマーが複数ある場合の認識用
    timer = wx.Timer(panel, ID_TIMER)         #timerをpanelに設置 ※インスタンス作成  ※タイマーイベントobjを出力している
    panel.Bind(wx.EVT_TIMER, OnTimer)         #EVT_TIMERはtimerから発生するイベトをキャッチ → OnTimer呼出し
    Speed = 1                                 #timerイベントの発生間隔  ※ブロック落下速度
    timer.Start(Speed)                        #Speedの間隔で(wx.EVT_TIMER)信号を発生 → OnTimer()をコールバック
    frame.Center()
    frame.Show()

if __name__ == '__main__':
    import wx
    import copy
    import random
    app = wx.App()
    Main()
    app.MainLoop()
