# -*- coding: utf-8 -*-

def SetBlockOnBoard(set_board, block_coords, x, y, block_shape): #boardにblock_shapeを配置
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        set_board[piece_y][piece_x] = block_shape

def DrawBlock(copy_board, block_coords, x, y, block_shape):      #ブロックを描写
    print('DrawBlock + SetBlockOnBoard')
    global board
    global curBlockCoords, curShape, curX, curY

    SetBlockOnBoard(copy_board, block_coords, x, y, block_shape)
    board = copy.deepcopy(copy_board)
    curBlockCoords = copy.deepcopy(block_coords)
    [curShape, curX, curY] = [block_shape, x, y]
    panel.Refresh()

def CheckMoveAvailable(check_board, block_coords, x, y):
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        if piece_x < 0 or piece_x > BoardWidth - 1 or\
            piece_y < 0 or piece_y > BoardHeight - 1 or\
                check_board[piece_y][piece_x] != 0:
            return False
    return True

def CheckDelLine(check_board):
    delLineNumb = BoardHeight
    for i in range(BoardHeight):
        if not (0 in check_board[i]):
            delLineNumb = i
    return delLineNumb

def OnKeyDown(event):
    global isCurBlock, isKeyDown

    if keyAllowed is False or isKeyDown is True:
        return
    #この時点でisKeyDown = False
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
            while nextY < BoardHeight - 1:
                if not CheckMoveAvailable(copy_board, nextBlockCoords, nextX, nextY + 1):
                    break
                nextY = nextY + 1
        if CheckMoveAvailable(copy_board, nextBlockCoords, nextX, nextY):
            DrawBlock(copy_board, nextBlockCoords, nextX, nextY, curShape)
            isCurBlock = True
    isKeyDown = False

def OnTimer(event):
    print('OnTimer')
    global isCurBlock, keyAllowed, isKeyDown, board

    if event.GetId() != ID_TIMER or isKeyDown is True:
        return

    keyAllowed = False
    copy_board = copy.deepcopy(board)

    if not isCurBlock:
        delLineNumb = CheckDelLine(copy_board)
        if delLineNumb >= 0 and delLineNumb <= BoardHeight - 1:
            del board[delLineNumb]
            board.insert(0, [0] * BoardWidth)
            panel.Refresh()                   #行を削除する際に実行される
        else:
            newShape = random.randint(1, 7)
            newBlockCoords = copy.deepcopy(BlockTable[newShape])
            [newX, newY] = [5, 1]   #y軸が0でなく1の理由、ブロック雛形(y軸-1～+2)、y=-1の場合を考慮しなければならない
                                    #ブロックの座標(x,y)初期値が発生
            if not CheckMoveAvailable(copy_board, newBlockCoords, newX, newY):
                event.GetTimer().Stop()
                yesno = wx.MessageBox('もう一度始めますか？', '', wx.YES_NO)
                if yesno == wx.YES:
                    board = []
                    for i in range(BoardHeight):
                        board.append([0] * BoardWidth)
                    [isCurBlock, keyAllowed, isKeyDown] = [False] * 3
                    Speed = 50
                    event.GetTimer().Start(Speed)
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
    print('OnPaint')
    obj = event.GetEventObject()
    dc = wx.BufferedPaintDC(obj)        #イベント発生 => def OnEraseBackground() => Bufferにデータ蓄積 => 描写実行 => Clear()
    #print("{0}をClearしたよ".format(dc))
    dc.Clear()                          #dc = wx.BufferedPaintDCインスタンスobjを消去

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

def OnEraseBackground(event):                                #描写を消去するイベントを処理
    print('OnEraseBackground')

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

    [isCurBlock, keyAllowed, isKeyDown] = [False] * 3

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

    BlockTable = [ShapeNo, ShapeZ, ShapeS, ShapeLine, ShapeT, \
        ShapeSquare, ShapeL, ShapeMirroredL]
    #print('BlockTable[3][3]=', BlockTable[3][3])
    #print('BlockTable[3][3][0]=', BlockTable[3][3][0])
    #print('BlockTable[3][3][1]=', BlockTable[3][3][1])

    colors = ['BLACK', wx.Colour('RED'), wx.Colour('GREEN'), \
        wx.Colour('BLUE'), wx.Colour('YELLOW'), wx.Colour('CYAN'), \
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

    frame = wx.Frame(None, title='TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    panel.Bind(wx.EVT_PAINT, OnPaint)                      #Refresh(再描写)に発生
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground) #Refresh、Clear で発生
    ID_TIMER = 1
    timer = wx.Timer(panel, ID_TIMER)
    panel.Bind(wx.EVT_TIMER, OnTimer, id=ID_TIMER)         #timer.speed(100)毎に発生
    Speed = 100
    timer.Start(Speed)
    panel.Bind(wx.EVT_CHAR_HOOK, OnKeyDown)                #キー押下時に発生
    frame.Center()
    frame.Show()

if __name__ == '__main__':
    import wx
    import copy
    import random
    app = wx.App()
    Main()
    app.MainLoop()



#def OnEraseBackground()      ※frame.Center()
#↓
#def OnEraseBackground()      ※frame.Show()
#↓
#app.MainLoop()
#↓
#def OnPaint()
#↓
#def OnTimer()    => time毎の実行(EVT発生=>OnTimer) ※行消去 or 新規Block or Block落下
#↓
# def DrawBlock() => Refresh(EVT発生=>OnPaint)
#↓
#def OnPaint()    => wx.BufferedPaintDC()  ※旧パネル消去(EVT発生=>OnEraseBackground) + 新パネル描写
#↓
# def OnEraseBackground()
#↓
#def OnTimer()    => time毎の実行(EVT発生=>OnTimer) ※行消去 or 新規Block or Block落下
#↓
# def DrawBlock() => Refresh(EVT発生=>OnPaint)
#↓
#def OnPrint()    => wx.BufferedPaintDC()  ※旧パネル消去(EVT発生=>OnEraseBackground) + 新パネル描写
#↓
# def OnEraseBackground()
#↓
#def OnTimer()    => time毎の実行(EVT発生=>OnTimer) ※行消去 or 新規Block or Block落下
#↓
# def DrawBlock() => Refresh(EVT発生=>OnPaint)
#↓
#def OnPaint()    => wx.BufferedPaintDC()  ※旧パネル消去(EVT発生=>OnEraseBackground) + 新パネル描写
#↓
# def OnEraseBackground()
#↓
#def OnTimer()    => time毎の実行(EVT発生=>OnTimer) ※行消去 or 新規Block or Block落下
#↓
# def DrawBlock() => Refresh(EVT発生=>OnPaint)
#↓
#def OnPaint()    => wx.BufferedPaintDC()  ※旧パネル消去(EVT発生=>OnEraseBackground) + 新パネル描写
#↓
# def OnEraseBackground()


#[
#[[0, 0], [0, 0], [0, 0], [0, 0]],
#[[0, -1], [0, 0], [-1, 0], [-1, 1]],
#[[0, -1], [0, 0], [1, 0], [1, 1]],
#[[0, -1], [0, 0], [0, 1], [0, 2]],
#[[-1, 0], [0, 0], [1, 0], [0, 1]],
#[[0, 0], [1, 0], [0, 1], [1, 1]],
#[[-1, -1], [0, -1], [0, 0], [0, 1]],
#[[1, -1], [0, -1], [0, 0], [0, 1]]
#]
#要素を取り出すには、BlockTable[i][j][k] ※三次元配列