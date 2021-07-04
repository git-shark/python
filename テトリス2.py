# -*- coding: utf-8 -*-
from pdb import set_trace

# pythonはプログラムを走らせると変数__name__に文字列'__main__'を自動的に代入する
# プログラムが直接起動した場合の判定、コマンドラインやファイルからの起動時にTrueとなる
# __main__、すなわちファイルやコマンドラインから直接起動したよ。の意味
# 他のプログラムから呼ばれた場合は、そのプログラム名が代入される

# イベント発生により処理をさせる = イベントドリブン
# その処理を担当するプログラム = イベントハンドラ(コールバック関数)

# board 0-9 or 0-21
# PieceSize = サイズは20、描写は0-19の値をとる
# y+(piecesize-1)=19を示す piecesizeは0-19で描写されている

#cur	    カー          雑種
#coords	    コーズ        領域
#Available	アベイラブル  利用可能な空白
#allowed	アラウド      許容

def SetBlockOnBoard(set_board, block_coords, x, y, block_shape):  #boardにblockcoordsを代入
    for i in range(4):                                            #range(-1,3)にすると走る
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        try:
            set_board[piece_y][piece_x] = block_shape
        except:
            pass
        #print('x',piece_x)
        #print('y',piece_y)
        #print(block_shape)

def DrawBlock(copy_board, block_coords, x, y, block_shape):       #blockを描く
    global board
    global curBlockCoords, curShape, curX, curY

    SetBlockOnBoard(copy_board, block_coords, x, y, block_shape)
    board = copy.deepcopy(copy_board)
    curBlockCoords = copy.deepcopy(block_coords)
    [curShape, curX, curY] = [block_shape, x, y]
    try:
        panel.Refresh()                      #前データを削除し再描画  ※再描写後「描写メッセージ(EVT_PAINT)が発生」
    except:
        pass


def CheckMoveAvailable(check_board, block_coords, x, y):
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        if piece_x < 0 or piece_x > BoardWidth - 1 or\
            piece_y < 0 or piece_y > BoardHeight - 1 or\
                check_board[piece_y][piece_x] != 0:
            return False
    return True   #正誤箇所   ネストが一段深すぎ

def CheckDelLine(check_board):
    delLineNumb = BoardHeight             #初期値=22
    for i in range(BoardHeight):
        if not (0 in check_board[i]):
            delLineNumb = i
    return delLineNumb

def OnKeyDown(event):
    global isCurBlock, isKeyDown

    if keyAllowed is False or isKeyDown is True: return

    isKeyDown = True

    keycode = event.GetKeyCode()

    if keycode == wx.WXK_LEFT or keycode == wx.WXK_RIGHT or\
        keycode == wx.WXK_DOWN or keycode == wx.WXK_UP or\
            keycode == wx.WXK_SPACE:
        copy_board = copy.deepcopy(board)
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)
        nextBlockCoords = copy.deepcopy(curBlockCoords)
        [nextX, nextY] = [curX, curY]

        if keycode == wx.WXK_LEFT:
            nextX = curX - 1
        elif keycode == wx.WXK_RIGHT:
            nextX = curX + 1
        elif keycode == wx.WXK_DOWN:
            for i in range(4):
                nextBlockCoords[i][0] = -curBlockCoords[i][1]
                nextBlockCoords[i][1] = curBlockCoords[i][0]
        elif keycode == wx.WXK_UP:
            for i in range(4):
                nextBlockCoords[i][0] = curBlockCoords[i][1]
                nextBlockCoords[i][1] = -curBlockCoords[i][0]
        elif keycode == wx.WXK_SPACE:
            while nextY < BoardHeight:
                if not CheckMoveAvailable(copy_board, curBlockCoords, nextX, nextY + 1):
                    break
                nextY = nextY + 1

        if CheckMoveAvailable(copy_board, nextBlockCoords, nextX, nextY):
            DrawBlock(copy_board, nextBlockCoords, nextX, nextY, curShape)
            isCurBlock = True
    isKeyDown = False

def OnTimer(event):                                             #event=panel、慣例で仮引数には(event)表記を用いる
    global isCurBlock, keyAllowed                               #フラグ(描写判定用)グローバル化

    if event.GetId() != ID_TIMER or isKeyDown is True: return   #イベント発生源がpanelか否かの判定

    keyAllowed = False
    copy_board = copy.deepcopy(board)
    if not isCurBlock:
        delLineNumb = CheckDelLine(copy_board)
        if delLineNumb < BoardHeight and delLineNumb >= 0:
            del board[delLineNumb]
            board.insert(0, [0] * BoardWidth)
            panel.Refresh()
        else:
            newShape = random.randint(1, 7)
            newBlockCoords = copy.deepcopy(BlockTable[newShape])
            [newX, newY] = [int(BoardWidth / 2), 1]
            if not CheckMoveAvailable(copy_board, newBlockCoords, newX, newY):
                event.GetTimer().Stop()
                yesno = wx.MessageBox('もう一度始めますか？', '', wx.YES_NO)   #再スタート
                if yesno == wx.YES:
                    board = []
                    for i in range(BoardHeight):
                        board_row = [0] * BoardWidth
                        board.append(board_row)
                    [isCurBlock, keyAllowed, isKeyDown] = [False] * 3
                    Speed = 10
                    event.GetTimer().Start(Speed)
                return
            else:
                DrawBlock(copy_board, newBlockCoords, newX, newY, newShape)
                isCurBlock = True
    else:
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)            #前回の描写を消去
        if not CheckMoveAvailable(copy_board, curBlockCoords, curX, curY+1):  #最下段到達後に更に落とせの指示が入っている？
            isCurBlock = False
        else:
            DrawBlock(copy_board, curBlockCoords, curX, curY + 1, curShape)
    keyAllowed = True

def OnPaint(event):                            #paintはここで描写に使用、描写直前まで意図しない挙動とならぬようcopy_boardで各作業を行う
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
                dc.DrawLine(x + 1, y + PieceSize - 1,\
                    x + PieceSize - 1, y + PieceSize - 1)
                dc.DrawLine(x + PieceSize - 1, y + 1,\
                    x + PieceSize - 1, y + PieceSize - 1)

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
    global isCurBlock, keyAllowed, isKeyDown
    global panel
    global ID_TIMER, timer

    [PieceSize, BoardWidth, BoardHeight] = [20, 10, 22]
    PanelWidth = PieceSize * BoardWidth
    PanelHeight = PieceSize * BoardHeight

    #表記 = [[x,y],[x,y],[x,y],[x,y]]
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
    dark = ['BLACK']
    for i in range(1, 8):
        light.append(colors[i].ChangeLightness(150))
        dark.append(colors[i].ChangeLightness(50))

    board = []

    for i in range(BoardHeight):
        board_row = [0] * BoardWidth
        board.append(board_row)
    [isCurBlock, keyAllowed, isKeyDown] = [False] * 3

    frame = wx.Frame(None, title='TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    panel.Bind(wx.EVT_PAINT, OnPaint)                 #panel.Refresh()実行 => (EVT_PAINT)が発生 => OnPaint関数へ
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)
    ID_TIMER = 1
    timer = wx.Timer(panel, ID_TIMER)                 #panelのIDを1としている
    panel.Bind(wx.EVT_TIMER, OnTimer, id=ID_TIMER)    #タイマーイベント発生毎に、コールバック関数OnTimeを実行
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


#line 76
#in OnTimer
#DrawBlock(copy_board, curBlockCoords, curX, curY + 1, curShape)

#line 13
#in DrawBlock
#SetBlockOnBoard(copy_board, block_coords, x, y, block_shape)

#line 7
#in SetBlockOnBoard
#set_board[piece_y][piece_x] = block_shape

#IndexError: list index out of range