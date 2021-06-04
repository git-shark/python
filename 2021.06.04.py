#-*- coding:utf-8 -*-
import sys

list = []
for i in range(1,100):
    if i % 12 == 0:
        list.append(i ** 2)
print(list)

list = [i ** 2 for i in range(1,100) if i % 12 == 0]
print(list)

dict = {i : i ** 2 for i in range(1,10)}
print(dict)

fp = open("text.txt","r")
content = fp.read()
print(content)
fp.close()

fp = open("text.txt","r")
for i in fp:
    print(i)
fp.close()

fp = open("text.txt","r")
list = fp.readlines()
print(list)
fp.close()

# ※pythonはOSがwindowsの場合はデフォルトでShift_JISでデコードする
# UTF-8などのファイルを読み込む場合、エンコードを指定する必要がある

content = """
    ぐおお
    ぶりぶり
    うはw\
"""
fp = open("text.txt","a")
fp.write(content)
fp.close()

fname = "text2.txt"

try:
    fp = open(fname,"r")
    content = fp.read()
    fp.close()
#except FileNotFoundError as e:
 #   e = str(e)
  #  print(e)
   # print(e+"のエラーが起きました\n"+fname+"は見つかりませんでした")
except UnicodeDecodeError:
    print(fname+"のデコードができませんでした")
except Exception as e:
    e = str(e)
    print(fname+"において"+e+"が発生しました")
finally:
    print("うおお、ぶりぶりぶり")

with open("text.txt","r") as fp:
    content = fp.read()
    print(content)

print(sys.argv)

for arg in sys.argv:
    print(arg)
    