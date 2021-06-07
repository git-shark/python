class Test:
    def __init__(self, pub_val = "pub", pri_val = "pri"):
        self.pub_val = pub_val
        self.__pri_val = pri_val

    def set_pri_val(self, pri_val = "pri"):
        self.__pri_val = pri_val

    def get_pri_val(self):
        return self.__pri_val

test = Test()
print(test.pub_val)
print(test.get_pri_val())
test.set_pri_val("PRI")
print(test.get_pri_val())

class ParentClass:

    parent_static_val = "親の静的変数"

    def __init__(self, parent_self_val = "親のインスタンス変数"):
        print("parentコンストラクタ")
        self.parent_self_val = parent_self_val

    def func_parent(self):
        print("parentメソッド")

class ChildClass(ParentClass):

    child_static_val = "子の静的変数"

    def __init__(self, child_self_val = "子のインスタンス変数"):
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
print(childClass.parent_self_val)