nlist = []

for i in range(10):
    n = int(input())
    m = n%42
    nlist.append(m)
print(len(set(nlist)))