import re

sentence = """\
電話番号は0120-0000-0000だったかな
あっ、でも0120-0-0000かも
いやいや確か0120-0000-0000だった\
"""
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
re_comp = re.compile(pattern)

rep_word = "[フリーダイヤル]"

match_iter = re.finditer(re_comp, sentence)
print("\n【文字列】 \n" + sentence + "\n")
print("【正規表現】 \n" + pattern + "\n")
#print("【\コンパイル】\n" + str(re_comp) + "\n")
print("【結 果】 \n" + ("-"*60))

loop_flag = False
for match in match_iter:
    print("group():{0}".format(match.group()))
    print("start():{0}".format(match.start()))
    print("end():{0}".format(match.end()))
    print("span():{0}".format(match.span()))
    print("-"*60)
    loop_flag = True

if not loop_flag:
    print("正規表現と一致しませんでした")

res = re_comp.sub(rep_word, sentence)
print(res)

set_1 = set((10, "テスト", 10, "てすと", "てスト"))
print(set_1)

set_1.clear()
print(set_1)