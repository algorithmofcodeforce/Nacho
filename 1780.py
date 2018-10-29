stopper = 1
nlist = []
while stopper == 1:
    temp = list(map(int,input().split()))
    if temp == [0]:
        break
    else:
        nlist.append(temp)
for i in range(len(nlist)):
    while len(nlist[i]) > 6:
