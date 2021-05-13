import sys

print("sys.exit()の前なので出力される")
input("EnterKeyでsys.exit()をexecute")
sys.exit(0)
print("sys.exit()後なので出力されない")
input("EnterKeyで終了 sys.exit()の後なので実行されない")

