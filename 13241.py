answer = []
m, n = map(int, input().split())
xnum = 2
mlist = []
nlist = []
alllist = []
while (m > 1):
    if m % xnum == 0:
        mlist.append(xnum)
        m = m / xnum
    else:
        xnum += 1
xnum = 2
while (n > 1):
    if n % xnum == 0:
        nlist.append(xnum)
        n = n / xnum
    else:
        xnum += 1
amount = 1
for i in range(len(mlist)):
    if mlist[i] in nlist:
        mlist[i] = 1
alllist = nlist + mlist

for i in range(len(alllist)):
    amount *= alllist[i]
answer.append(amount)
print(answer[0])