Count = int(input())
i = []
i = input().split()
ilist = []
point = 0
for j in range(1,len(i)-1):
    ilist[point] = int(i[0]) / int(i[j])
    point+= 1
print(i)