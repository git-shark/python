menu_list = ["1:加算","2:減算","3:乗算","4:除算","9:終了"]

def get_menu():
    for menu in menu_list:
        print(menu)
    ope = input("数値を入力してください=>")
    ope = int(ope)
    return ope

def do_calc(ope):
    ans = 0
    ope_word = ""

    if ope == 1:
        ans = num_1 + num_2
        ope_word = "+"
    elif ope == 2:
        ans = num_1 - num_2
        ope_word = "-"
    elif ope == 3:
        ans = num_1 * num_2
        ope_word = "*"
    elif ope == 4:
        ans = num_1 / num_2
        ope_word = "/"

    return (ans, ope_word)

LOOP_MAX = 1
loop_cnt = 0

while loop_cnt < LOOP_MAX:
    ope = get_menu()

    if ope == 9:
        break

    num_1 = input("左辺=>")
    num_2 = input("右辺=>")

    num_1 = int(num_1)
    num_2 = int(num_2)

    ans, ope_word = do_calc(ope)

    msg_ans = "{num_1}{ope_word}{num_2}={ans}".format(num_1=num_1,ope_word=ope_word,num_2=num_2, ans=ans)
    print(msg_ans)
    print("-"*30)

    loop_cnt =+ 1

num_3 = 10
num_4 = 2

try:
    ans = num_3/num_4
    print("{1} / {2} = {0}".format(ans,num_3,num_4))
except ZeroDivisionError:   #例外が生じた場合   exceptを複数記述する事も可能
    print("{0} / {1} の計算において例外が発生しました".format(num_3,num_4))
except TypeError:
    print("Typeエラーが発生しました")
else:                       #例外が発生しなかった時
    print("正常に処理されました")
finally:                    #条件に関係なく実行される
    print("強制処理部分")

try:
    raise NameError("意図的な")
except ZeroDivisionError:
    print("{0}:ZeroDivisionError".format(e))
except TypeError as e:
    print("{0}:TypeError".format(e))
except NameError as e:
    print("{0}:NameError".format(e))
except Exception as e:
    print("{0}:Exeption".format(e))
