#-*- coding:utf-8 -*-
import sys
import os
import re

try:
    for r_file_path in sys.argv[1:]:
        base,ext = os.path.splitext(r_file_path)
        w_file_path = base + "_done" + ext
        r_content = ""
        with open(r_file_path,"r") as r_fp:
            r_content = r_fp.read()
            w_content = re.sub("[0-9]{4,8}","********",r_content)
            with open(w_file_path,"w") as w_fp:
                w_fp.write(w_content)
            print("読込:" +r_file_path)
            print("出力:" +w_file_path)
            print("-"*30)
except Exception as e:
    print(str(e)+"が発生しました")

print((lambda num: num * num)(5))

lamb_jyou = lambda num_1, num_2 = 2: num_1 ** num_2
print(lamb_jyou(5))
print(lamb_jyou(5,3))

def func_conv(val):
    if "z" in val:
        res = val.title()
    else:
        res = val.upper()
    return res

print(func_conv("hello world"))

print((lambda val : val.title() if " " in val else val.upper()) ("hellw world"))
    # (lambda val : val.title() if " " in val else val.upper()) ("hello world")

def func_conv(val):
    if " " in val:
        res = val.title()
    else:
        res = val.upper()
    return res

req_list = ["hello",
        "WORLD",
        "helloworld",
        "heLLw world",
        "hello world"]

for res in map(func_conv, req_list):
    print(res)

for res in map(lambda val : val.title() if val in " " else val.upper(), req_list):
    print(res)

for res in map(lambda val : val.title() if val in " " else val.upper(), req_list):
    print(res)