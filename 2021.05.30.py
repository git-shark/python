import re

list = [1, 2, 3]

flag = True

if not flag:
    for lists in list:
        lists = str(lists)
        print("not True = " +lists)

flag = False

if not flag:
    for lists in list:
        lists = str(lists)
        print("not False = " +lists)

print("not True = " + str(not True))    #not Trueとは  ※Trueではない = 排他的結論、すなわちFalse

print("not False = " + str(not False))

print("""\
ぶりぶりうわああ""")

sentence = """\
    電話
    番号
    うわ
    ああ\
    """

print(sentence)

#""" 数行 """ について。  各行に表記したデータの改行コード(\n)も含めて反映される

#(\ = 継続文字) バックスラッシュ直後の改行コードを1回分無視する
#最初の """ のあとで改行してから書き出したいが、文字列の先頭に改行を含めたくないので """ の直後に \ を記述している

