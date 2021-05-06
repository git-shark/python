#学習
#listやtupleに値を代入する際の注意
#文字扱いの場合はクオーテーションで囲む必要あり

list = [
    1,
    2,
    3,
    4,
    5,
    6,
    "f"]

tuple = (
    "a",
    "b",
    "c"
)

for list_data in list:
    print(list_data)

for tuple_data in tuple:
    print(tuple_data)