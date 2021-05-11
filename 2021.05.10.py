list = ["ABC","DED","GHI"]
max = 3
cnt = 1
while cnt <= max:
    print("{0}times".format(cnt))
    for val in list:
        print(val)
    print("")
    cnt += 1

cnt_1 = 1
cnt_2 = 1
cnt_3 = 1
msg = ""

while cnt_1 <= 3:
    while cnt_2 <= 3:
        while cnt_3 <= 3:
            msg += "{cnt_1}{cnt_2}{cnt_3} ".format(cnt_1 = cnt_1,cnt_2 = cnt_2,cnt_3 = cnt_3)
            cnt_3 += 1
        cnt_3 = 1
        msg += "\n"
        cnt_2 += 1
    cnt_2 = 1
    cnt_1 += 1
print(msg)

#list,tuple 型 = 配列
#dictionary 型 = 連想配列
#items() key+value
#keys() key
#values() value

#dict_1 = {"key_1-1":"value_1-1","key_1-2":"value_1-2","key_1-3":"value_1-3"}
#two_dict = {"key_1":dict_1}
#print(two_dict)

dict_1 = {"key1":10,"key2":20,"key3":30}
two_dict = {"key1":dict_1}
print(two_dict)
#計算できる数値以外は文字列扱い""で囲う必要あり

dict_2 = {"0":1,"1":2,"2":3}
third_dict = {"key":dict_2}
print(third_dict)


#【飯類】
#・チャーハン
#・ピラフ
#・マーボー丼

rice_list = ["チャーハン","ピラフ","マーボー丼"]
bread_list = ["サンドイッチ","バタートースト","フランスパン"]
noodle_list = ["ラーメン","パスタ","焼きそば"]

food_type = {"飯類":rice_list,"パン類":bread_list,"麺類":noodle_list}

for type, list in food_type.items():
    print("【{0}】".format(type))
    for food in list:
        print("{0}".format(food))
    print("\n")