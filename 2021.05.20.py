color = "red,green,blue,yellow,cyan,magenta"

color_list = color.split(",")
print(color_list)

color_list = color.split(",",1)
print(color_list)

color_list = color.split(",",4)
print(color_list)

sentence = """\
あいうえお
かきくけこ
さしすせそ


たちつてと
なにぬねの\
"""

sentence_list = sentence.splitlines()
print(sentence_list)

sentence_list = sentence.splitlines(True)
print(sentence_list)

print(color.replace("ed", "oooo"))

key_word = "あかさたなはまやらわをん"
trans_table = str.maketrans("あか","おお","わをん")   #第一,第二引数に文字数差があるとエラー。※第三引数は文字数に関係しない
print(key_word.translate(trans_table))

print(key_word.strip("あさなまらを"))     #必ず左端から順にデータを削除する、削除できない部分が残ると終了
print(key_word.lstrip("あさ"))           #必ず左端から順にデータを削除する、削除できない部分が残ると終了
print(key_word.rstrip("んわ"))           #必ず右端から順にデータを削除する、削除できない部分が残ると終了
