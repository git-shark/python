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

def power_gene():
    for num in range(1, 4):
        print("{0}の{0}乗".format(num))
        yield num ** num

for res in power_gene():
    pass

print("-" * 30)

for res in power_gene():
    print(res)

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

def power_gene3():
    num = 1
    while True:
        yield num ** num
        num += 1
for res in power_gene3():
    if res > 100000:
        break
    print(res)

def color_gene():
    yield "red"
    yield "green"
    yield "blue"
    yield "yellow"
    yield "cyan"
    yield "magent"
cg = color_gene()
print(next(cg))
print(next(cg))
print(next(cg))
print(next(cg))
print(next(cg))
print(next(cg))

pg2 = [i ** i for i in range(1, 4)]
print(pg2)

pg3 = (num * num for num in range(1,6))
print(next(pg3))
print(next(pg3))
print(next(pg3))
print(next(pg3))
