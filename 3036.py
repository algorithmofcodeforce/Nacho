Count = int(input())
i = []
i = list(input().split())

ilist = []
for j in range(len(i)):
    i[j] = int(i[j])
for j in range(len(i)):
    ilist.append(i[j])
for j in range(len(i)):
    i[j] = int(i[j])

for num in range(1,Count):
    for j in range(len(ilist)):
        i[j] = ilist[j]
    if i[0] % i[num] == 0:
        print(i[0]//i[num],end='/1')
        print("")
        ######
    elif i[0] % i[num] != 0:
        k = 2
        while k < i[0]and k < i[num]:
            if i[0]%k ==0 and i[num]%k==0:
                i[0] = i[0]//k
                i[num] = i[num]//k
            else:
                k += 1
        print(i[0],end='/')
        print(i[num])

