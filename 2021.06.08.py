color_list = ["red", "green", "blue", "yellow", "cyan", "magenta"]
color_iter = iter(color_list)
print(next(color_iter))
print(next(color_iter))
print("-"*10)
for color in color_iter:
    print(color)
print("-"*30)

class PowerIter:
    def __init__(self, val):
        self.val = val
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num > self.val:
            raise StopIteration
        res = self.num ** self.num
        self.num += 1
        return res

powerIter = PowerIter(10)
for p in powerIter:
    print(p)

print("-"*30)

def power_gene():
    for num in range(1, 4):
        print("{0}の{0}乗".format(num))
        yield num ** num

for res in power_gene():
    pass

print("-"*30)

for res in power_gene():
    print(res)

print("-"*30)

def power_gene2():
    num = 1
    while True:
        yield num ** num
        num += 1
pg = power_gene2()
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))

print("-"*30)

def power_gene3():
    num = 1
    while True:
        yield num ** num
        num += 1
for res in power_gene3():
    if res >= 100000:
        break
    print(res)

power_gene3()

print("-"*30)