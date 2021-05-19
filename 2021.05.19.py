# -*- coding: utf-8 -*-
import sys
#sys.path.append("/Users/shark/git/python")
import my_func

menu_list = ["1:加算","2:減算","3:乗算","4:除算","5:終了"]

ope_word_list = ["+","-","*","/"]

def get_menu():
    for menu in menu_list:
        print(menu)

    ope = my_func.input_int("数値を入力してください=>")

    return ope

def do_calc(ope):
    ans = 0
    ope_word = ""

    if ope == 1:
        ans = num_1 + num_2
        ope_word = ope_word_list[0]
    elif ope == 2:
        ans = num_1 - num_2
        ope_word = ope_word_list[1]
    elif ope == 3:
        ans = num_1 * num_2
        ope_word = ope_word_list[2]
    elif ope == 4:
        ans = num_1 / num_2
        ope_word = ope_word_list[3]

    return (ans, ope_word)

LOOP_MAX = 5
loop_cnt = 0

while loop_cnt < LOOP_MAX:
    ope = get_menu()

    if ope == 5:
        break

    if ope is None or ope < 1 or ope > 4:
        print("1〜5を入力してください")
        continue

    num_1 = my_func.input_int("左辺 =>")
    num_2 = my_func.input_int("右辺 =>")

    if num_1 is None or num_2 is None:
        print("数値を入力してください")
        continue

    try:
        ans, ope_word = do_calc(ope)
    except Exception as e:
        print("例外が発生しました:{0}".format(e))
        sys.exit(1)

    msg_ans = "{num_1}{ope_word}{num_2}={ans}".format(num_1=num_1,num_2=num_2,ope_word=ope_word,ans=ans)
    print(msg_ans)

    print("-"*60)

    loop_cnt += 1

input("Enterキーで終了")
