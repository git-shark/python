import sys

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

    num_1 = input("左辺を入力してください=>")
    num_2 = input("右辺を入力してください=>")

    num_1 = int(num_1)
    num_2 = int(num_2)

    try:
        ans,ope_word = do_calc(ope)
    except Exception as e:
        print("例外が発生しました:{0}".format(e))
        sys.exit(1)

    msg_ans = "{num_1}{ope_word}{num_2} = {ans}".format(num_1=num_1,ope_word=ope_word,num_2=num_2,ans=ans)

    print(msg_ans)

    print("-"*60)

    loop_cnt += 1

input("Enterキーで終了")