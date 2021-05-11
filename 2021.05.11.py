
LOOP_MAX = 3
loop_cnt = 0

ope_menu = ["加算:1","減算:2","乗算:3","除算:4","終了:9"]

while loop_cnt < LOOP_MAX:
    for menu in ope_menu:
        print(menu)

    ope = 0

    ope = input("数値を入力してください=>")
    ope = int(ope)

    if 9 == ope:
        break

    ans = 0
    ope_word = ""

    num_left = input("左辺の数値を入力してください")
    num_left = int(num_left)

    num_right = input("右辺の数値を入力してください")
    num_right = int(num_right)

    if 1 == ope:
        ans = num_left + num_right
        ope_word = "+"
    elif 2 == ope:
        ans = num_left - num_right
        ope_word = "-"
    elif 3 == ope:
        ans = num_left * num_right
        ope_word = "*"
    elif 4 == ope:
        ans = num_left / num_right
        ope_word = "/"

    msg_ans = "{num_left}{ope_word}{num_right}={ans}".format(num_left=num_left,ope_word=ope_word,num_right=num_right,ans=ans)
    print(msg_ans)
    loop_cnt += 1

    print("-"*100)


