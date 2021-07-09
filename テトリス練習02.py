# -*- coding: utf-8 -*-

def SetBlockOnBoard(set_board, block_coords, x, y, block_shape):


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
    ShapeL = [[-1, 1], [0, -1], [0, 0], [0, 1]]
    ShapeMirroredL = [[1, -1], [0, -1], [0, 0], [0, 1]]

    BlockTable = [ShapeNo, ShapeZ, ShapeS, ShapeLine, \
        ShapeT, ShapeSquare, ShapeL, ShapeMirroredL]

    colors = ['BLACK', wx.Colour('RED'), wx.Colour('GREEN'), \
        wx.Colour('BLUE'), wx.Colour('YELLOW'), wx.Colour('CYAN'), \
            wx.Colour('LIGHT_BLUE'), wxColour('VIOLET_RED')]

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
    panel.Bind(wx.EVT_PAINT, OnPaint)
    panel.Bind(wx.EVT_ERASE_BACKGROUND, OnEraseBackground)
    panel.Bind(wx.EVT_CHAR_HOOK, OnKeyDown)
    ID_TIMER = 1
    timer = wx.Timer(panel, ID_TIMER)
    panel.Bind(wx.EVT_TIMER, OnTimer, id = ID_TIMER)
    Speed = 100
    timer.Start(Speed)
    frame.Center()
    frame.Show()

if __name__ == '__main__':
    import wx
    import copy
    import random
    app = wx.App()
    Main()
    app.MainLoop()