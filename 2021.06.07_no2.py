class ParentClass:
    parent_static_val = "親の静的変数"
    def __init__(self, parent_self_val = "親インスタンスの値"):
        print("parentコンストラクタ")
        self.parent_self_val = parent_self_val
    def func_parent(self):
        print("parentメソッド")

class ChildClass(ParentClass):
    child_static_val = "子の静的変数"
    def __init__(self, child_self_val = "子インスタンスの値"):
        super().__init__()
        print("childコンストラクタ")
        self.child_self_val = child_self_val
    def func_child(self):
        print("childメソッド")

childClass = ChildClass()
print(ParentClass.parent_static_val)
print(ChildClass.child_static_val)

childClass.func_child()
childClass.func_parent()

print(childClass.child_static_val)
print(childClass.parent_static_val)

print(childClass.child_self_val)
print(childClass.parent_self_val)  #この値を得るには、子クラスから明示的に親クラスの初期化を促さなければならない
                                   #super().__init__()を使用する