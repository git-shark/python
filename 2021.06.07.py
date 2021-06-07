#self = 自分自身  ※(classであれば、それそのもの)
#コンストラクタ(__init__ )= インスタンスを新規作成する際の初期化の役目

class Color:
    def __init__(self, text = "red"):
        print("初期化されました =>  " + str(self))
        self.text = text

    def __del__(self):
        print("破棄されました =>  " + str(self))

color = Color()
print(color.text)

color.text_2 = "green"
color.text_3 = "black"

print(color.text_2)
print(color.text_3)

class Color_2():
    def __init__(self, r_name = "red", g_name = "green", b_name = "blue"):
        self.r_name = r_name
        self.g_name = g_name
        self.b_name = b_name
        print("初期化されました =>  " + str(self))

    def name_print(self, delim = ","):
        print("{r}{delim}{g}{delim}{b}".format(r = self.r_name, g = self.g_name, b = self.b_name, delim = delim))

    def __del__(self):
        print("破棄されました =>  " + str(self))

color2 = Color_2()
color2.name_print("-")

color3 = Color_2("赤", "緑", "青")
color3.name_print("|")

color4 = Color_2(g_name = "black")
color4.name_print("+")

color2 = Color_2()
color2.name_print("-")

class Test:
    def __init__(self, pub_val = "pub", pri_val = "pri"):
        self.pub_val = pub_val
        self.__pri_val = pri_val

    def get_pri_val(self):
        return self.__pri_val

test = Test()
print(test.pub_val)
print(test.get_pri_val())
#pri_val = test.get_pri_val()
#print(pri_val)

test.__pri_val = "PRI"
print(test.__pri_val)

print(test.get_pri_val())

