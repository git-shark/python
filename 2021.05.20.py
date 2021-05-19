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