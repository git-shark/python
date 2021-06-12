global_val = "global"
if True:
    print("0:{0}".format(global_val))
    global_val = "local"
    local_val = "local"
    print("1:{0}".format(global_val))
    print("2:{0}".format(local_val))
print("3:{0}".format(global_val))
print("4:{0}".format(local_val))

global_val2 = "global"
for i in ["1回だけループ用"]:
    print("0:{0}".format(global_val2))
    global_val2 = "local"
    local_val2 = "local"
    print("1:{0}".format(global_val2))
    print("2:{0}".format(local_val2))
print("3:{0}".format(global_val2))
print("4:{0}".format(local_val2))

global_val3 = "global"
def scope_test():
    print("0:{0}".format(global_val3))
scope_test()

global_val4 = "global"
def scope_test2():
    global_val4 = "local"
    local_val4 = "local"
    print("1:{0}".format(global_val4))
    print("2:{0}".format(local_val4))
scope_test2()
print("3:{0}".format(global_val4))
#print("4:{0}".format(local_val4))

global_val_1 = "global"
global_val_2 = "global"
def scope_test3():
    global global_val_1
    global_val_1 = "local"
    global_val_2 = "local"
scope_test3()
print("global_val_1 : {0}".format(global_val_1))
print("global_val_2 : {0}".format(global_val_2))

def scope_test4():
    val_1 = "val_1"
    val_2 = "val_2"
    def scope_test_inner():
        nonlocal val_1
        val_1 = "val_10"
        val_2 = "val_20"
    scope_test_inner()
    return val_1, val_2
res = scope_test4()
print(res)

global_val = "global"
def scope_test():
    print("0:{0}".format(global_val))
    global_val = "local"
    local_val = "local"
    print("1:{0}".format(global_val))
    print("2:{0}".format(local_val))
scope_test()
print("3:{0}".format(global_val))
print("4:{0}".format(local_val))