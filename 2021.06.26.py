import copy

list_a = [0, 1, 2]
print(id(list_a))            #>>>2468344264192
list_b = list_a
print(id(list_b))            #>>>2468344264192
list_a = [00000, 11, 22]     # 値に(00000)と入力しても(0)として扱われる
print(id(list_a))            #>>>2468344289984
print(id(list_b))            #>>>2468344264192
                             #注意 :【list_aの格納アドレスが異なる】

list_c = list_a
print(id(list_a))            #>>>2468344289984
list_a[1] = 111
print(id(list_a))            #>>>2468344289984
print(id(list_c))            #>>>2468344289984
                             #注意 :【list_aの格納アドレスは同じ】

# 変更可  (ミュータブル)  ：リスト、セット、ディクショナリ、bytearray型
# 変更不可(イミュータブル)：タプル、数値型、文字列、ブール型、フローズンセット、bytes型

list_d = [[0, 1], [2, 3]]
list_e = copy.copy(list_d)
print(id(list_d))
print(id(list_e))
list_d[1] = [4, 5]
print(id(list_e))
list_d[0][1]=6
print(id(list_e))