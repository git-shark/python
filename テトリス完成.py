# -*- coding: utf-8 -*-
from pdb import set_trace

#【__name__と'__main__について】
# pythonはプログラムを走らせると変数__name__に文字列'__main__'を自動的に代入する
# プログラムが直接起動(コマンドライン、ファイル)からの場合、
# 自動で__name__に文字列'__main__が代入される
# __main__とは「ファイルやコマンドラインから直接起動したよ」の意味
# ※それ以外からの起動では、そのプログラム名が__name__に代入される

#isとは、オブジェクト同士を比較する演算子である
#x=[1, 2]
#y=[1, 2]
# x == y => True
# x is y => False

# イベント発生 → 処理 = イベントドリブン
# 処理プログラム      = イベントハンドラ (コールバック関数)

# board = list型 0-9 or 0-21 の範囲をとる
# 描写直前まで意図しない挙動を避けcopy_boardで作業を行う

#【関数】
#obj.GetEventObject = イベントを発生したオブジェクトを取得するメソッド

#【フラグ種】
#isCurBlock = ブロック描写フラグ
#keyAllowed = 一連的なkey処理の状態
#isKeyDown  = keyの1入力のみを受付  ※連続的key入力 → 処理終了まで他key入力を受付しない

#cur	    カー          雑種
#coords	    コーズ        領域
#Available	アベイラブル  利用可能な空白
#allowed	アラウド      許容
#row        ロウ          行

def SetBlockOnBoard(set_board, block_coords, x, y, block_shape):  #boardにblockcoordsを代入
    for i in range(4):
        piece_x = block_coords[i][0] + x
        piece_y = block_coords[i][1] + y
        set_board[piece_y][piece_x] = block_shape

def DrawBlock(copy_board, block_coords, x, y, block_shape):       #blockを描く
    global board
    global curBlockCoords, curShape, curX, curY

    SetBlockOnBoard(copy_board, block_coords, x, y, block_shape)
    board = copy.deepcopy(copy_board)
    curBlockCoords = copy.deepcopy(block_coords)
    [curShape, curX, curY] = [block_shape, x, y]
    panel.Refresh()                                         #前データ削除後の「再描画」
                                                            #描写後「描写イベントメッセージ(EVT_PAINT)が発生」

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
                nextBlockCoords[i][0] = -curBlockCoords[i][1] #右辺の-curBlockCoords[x][x]で符号計算をしている(マイナス化)
                nextBlockCoords[i][1] = curBlockCoords[i][0]
                #print('0(+)',curBlockCoords[i][0])          ※チェック用
                #print('0(-)',-curBlockCoords[i][0])
                #print('1(+)',curBlockCoords[i][1])
                #print('1(-)',-curBlockCoords[i][1])
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

def OnTimer(event):                                      #event=panel、※慣例で仮引数(event)表記を用いる
    global isCurBlock, keyAllowed, isKeyDown, board      #各フラグをグローバル化

    if event.GetId() != ID_TIMER or isKeyDown is True:   #panelにBindされているイベント発生先の判定
        return

    keyAllowed = False
    copy_board = copy.deepcopy(board)

    if not isCurBlock:
        delLineNumb = CheckDelLine(copy_board)
        if delLineNumb < BoardHeight and delLineNumb != 0:
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
                    Speed = 200
                    event.GetTimer().Start(Speed)
                return
            else:
                DrawBlock(copy_board, newBlockCoords, newX, newY, newShape)
                isCurBlock = True
    else:
        SetBlockOnBoard(copy_board, curBlockCoords, curX, curY, 0)            #前回のブロックを消去
        if not CheckMoveAvailable(copy_board, curBlockCoords, curX, curY+1):
            isCurBlock = False
        else:
            DrawBlock(copy_board, curBlockCoords, curX, curY + 1, curShape)
    keyAllowed = True

def OnPaint(event):                  #event=panel
    obj = event.GetEventObject()     #obj = panel  ※GetEventObject()はイベント発生源のobjを取得
    print(wx.BufferedPaintDC(obj))
    dc = wx.BufferedPaintDC(obj)     #図形を描くキャンパスのobj(panel)を指定し描写も行う
                                     #wx.BufferdPaintDC(obj)処理開始 → for文 → wx.BufferdPaintDC処理終了(描写) → Clear
                                     #22回の内部処理がある為にパファに格納し最後に描写する ※チラつき防止
    #dc.Clear()                       #描写後のデータを削除している 落下1段毎にClearしている。Clear後はnoneになる
    print('消したよ=>', dc.Clear())

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
    print('終わり')

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
    #Shape_x = [[x,y],[x,y],[x,y],[x,y]]

    BlockTable = [ShapeNo, ShapeZ, ShapeS, ShapeLine, ShapeT,\
        ShapeSquare, ShapeL, ShapeMirroredL]

    colors = ['BLACK', wx.Colour('RED'), wx.Colour('GREEN'),\
        wx.Colour('BLUE'), wx.Colour('YELLOW'), wx.Colour('CYAN'),\
        wx.Colour('LIGHT BLUE'), wx.Colour('VIOLET RED')]

        #['BLACK', wx.Colour(255, 0, 0, 255), wx.Colour(0, 255, 0, 255),
        # wx.Colour(0, 0, 255, 255), wx.Colour(255, 255, 0, 255),
        # wx.Colour(0, 255, 255, 255), wx.Colour(191, 216, 216, 255),
        # wx.Colour(204, 50, 153, 255)]

    light = ['BLACK']
    dark = ['BLACK']
    for i in range(1, 8):
        light.append(colors[i].ChangeLightness(150))
        dark.append(colors[i].ChangeLightness(50))

    #print(light)↓   ※appendで追記しているのでlight[0]の'BLACK'も存在している
    #['BLACK', wx.Colour(255, 127, 127, 255), wx.Colour(127, 255, 127, 255),
    # wx.Colour(127, 127, 255, 255), wx.Colour(255, 255, 127, 255),
    # wx.Colour(127, 255, 255, 255), wx.Colour(223, 235, 235, 255),
    # wx.Colour(229, 152, 204, 255)]

    board = []

    for i in range(BoardHeight):
        board_row = [0] * BoardWidth
        board.append(board_row)

    frame = wx.Frame(None, title='TetGame')
    frame.SetClientSize(PanelWidth, PanelHeight)
    panel = wx.Panel(frame)
    panel.SetBackgroundColour('BLACK')
    panel.Bind(wx.EVT_PAINT, OnPaint)                 #panel.Refresh()実行 => (EVT_PAINT)が発生 => OnPaint関数へ ※コールバック関数
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)
    ID_TIMER = 1
    timer = wx.Timer(panel, ID_TIMER)                 #panelのIDを1としている
    panel.Bind(wx.EVT_TIMER, OnTimer, id=ID_TIMER)    #タイマーイベント発生毎に、コールバック関数OnTimeを実行
    Speed = 300                                       #ミリ秒
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