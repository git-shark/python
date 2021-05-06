#学習
#listやtupleに値を代入する際の注意
#文字扱いの場合はクオーテーションで囲む必要あり

list = [1, 2]

tuple = ("a","b")

dict = {"key":10,"キー":20,"きー":30}

for list_data in list:
    print(list_data)

for tuple_data in tuple:
    print(tuple_data)

for key in dict:
    value = dict[key]
    print("{key}:{value}".format(key=key,value=value))

for k,v in dict.items():
    print("{0}:{1}".format(k,v))

for key in dict.keys():
    print("key={0}".format(key))

for value in dict.values():
    print("value={0}".format(value))