#-*- coding: utf-8 -*-
import pyautogui as pag
pag.PAUSE = 2.5
pag.FAILSAFE = False

# position() = マウスポインタの現在座標
# size() = モニタ解像度を表示  (左上:0,0) (右下:x,y共に解像度から-1)
# moveTo() = マウスを指定座標に移動させる
# onScreen() = 指定座標内のマウスカーソル有無
# FAILSAFE True = 誤作動時の制御機構、デフォルトで有効状態 マウス位置がx0,y0になると例外発生(pyautogui.FailSafeException)
# PAUSE = GUI操作毎のポーズ(秒数) 、デフォルト値あり(0.1秒)

x, y = pag.position()
print("-"*10)
print(x, y)
print("-"*10)
print("解像度{0}".format(pag.size()))
print("-"*10)

x, y = (300, 300)
pag.moveTo(x, y)
print("moveToメソッドでマウス位置{0}に移動".format((x, y)))
print("-"*10)
print("画面上にマウス位置は「{0}」".format("ある" if pag.onScreen(x, y) else "ない"))
print("-"*10)
print("positionメソッドの返り値 : {0}".format(pag.position()))
print("-"*10)
print("2.5秒以内にマウスカーソルを左上端に移動してください")
pag.moveTo(100, 100)
print("-"*10)