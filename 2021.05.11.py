
menu_list = ["加算:1","減算:2","乗算:3","除算:4","終了:9"]

LOOP_MAX = 1
loop_cnt = 0

while loop_cnt < LOOP_MAX:
    for menu in menu_list:
        print(menu)
    ope = input("式を選んで下さい=>")
    ope = int(ope)

    if 9 == ope:
        break

    num_1 = input("左辺値の入力=>")
    num_2 = input("右辺値の入力=>")

    num_1 = int(num_1)
    num_2 = int(num_2)

    ans = 0
    ope_word = ""

    if 1 == ope:
        ans = num_1 + num_2
        ope_word = "+"
    elif 2 == ope:
        ans = num_1 - num_2
        ope_word = "-"
    elif 3 == ope:
        ans = num_1 * num_2
        ope_word = "*"
    elif 4 == ope:
        ans = num_1 / num_2
        ope_word = "/"

    msg_ans = "{num_1}{ope_word}{num_2}={ans}".format(num_1=num_1,ope_word=ope_word,num_2=num_2,ans=ans)
    print(msg_ans)
    print("-"*100)
    loop_cnt += 1

list = [100, 200, 300, 400, 500]

def func_average(prm_list):
    list_len = len(prm_list)
    sum = 0

    for num in prm_list:
        sum += num

    average = sum / list_len
    return sum, average

res = func_average(list)        #戻り値 = (1500, 300.0)
sum = func_average(list)[0]
average = func_average(list)[1]
print("{0}".format(res))
print("合計:={0}".format(sum))
print("平均:={0}".format(average))
