#学習1
#num_1 = input("num_1 =>")
#num_2 = input("num_2 =>")
#ans = int(num_1) + int(num_2)

#完成イメージから分解して考えて書くと良い
#(完成形)num_1(10)+num_2(20)=30
#num_1(      文字部分
#10          代入部分
#)+num_2(    文字部分
#20          代入部分
#)=          文字部分
#30          代入部分

#print("num_1("+str(num_1)+")+num_2("+str(num_2)+")="+str(ans))

#msg_ans = "num_1({index0})+num_2({index1})={index2}".format(index0=num_1,index1=num_2,index2=ans)

#ope = 0
#while ope != "1":
#    ope = input("終了するには1を入力して下さい =>")
#    if ope == "1":
#        break

LOOP_MAX = 5
loop_cnt = 0

while loop_cnt < LOOP_MAX:
    print("1:加算")
    print("2:減算")
    print("3:乗算")
    print("4:除算")
    print("9:終了")

    ope = input("番号を入力して下さい =>")
    ope = int(ope)

    if ope == 9:
        break
    num_1 = input("左辺=>")
    num_2 = input("右辺=>")

    num_1 = int(num_1)
    num_2 = int(num_2)

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

    msg_ans = "{num_1} {ope_word} {num_2} = {ans}".format(num_1=num_1, ope_word = ope_word, num_2 = num_2, ans = ans)
    print(msg_ans)

    print("-" * 30)
    loop_cnt += 1