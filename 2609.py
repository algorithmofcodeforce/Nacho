answer = []
m, n = map(int, input().split())
mn = m*n
mlist = []
nlist = []
alllist = []
i = 2
while m > 1:
    if m % i == 0:
        m = m // i
        mlist.append(i)
    else:
        i += 1

i = 2
while n > 1:
    if n % i == 0:
        n = n // i
        nlist.append(i)
    else:
        i += 1

for i in range(len(mlist)):
    for j in range(len(nlist)):
        if mlist[i] == nlist[j]:
            mlist[i] = 0
            alllist.append(nlist[j])
            nlist[j] = 0
gcd = 1
lcm = 1
for i in list(alllist):
    gcd *= i
lcm = mn // gcd
print(gcd)
print(lcm)