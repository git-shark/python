import copy

#=関数
#【値の変更が片方に影響する】
old_list = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
new_list = old_list
print(id(old_list))      #入れ物IDは同じ
print(id(new_list))      #入れ物IDは同じ
print(id(old_list[0]))   #内容物IDは同じ
print(id(new_list[0]))   #内容物IDは同じ
##入れ物と内容物の参照先が完全に同じ


#copy関数
#【値の変更が片方に影響する】
old_list = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
new_list = copy.copy(old_list)
print(id(old_list))      #入れ物IDは異なる
print(id(new_list))      #入れ物IDは異なる
print(id(old_list[0]))   #内容物IDは同じ
print(id(new_list[0]))   #内容物IDは同じ
#入れ物は異なる、内容物は同じ


#deepcopy関数
#【値の変更が片方に影響しない】
old_list = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
new_list = copy.deepcopy(old_list)
print(id(old_list))      #入れ物IDは異なる
print(id(new_list))      #入れ物IDは異なる
print(id(old_list[0]))   #内容物IDも異なる
print(id(new_list[0]))   #内容物IDも異なる
#入れ物と内容物の参照先が完全に異なる
