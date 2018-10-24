t = int(input())
cup = [1, 0, 0]
for i in range(t):
    n, m = map(int,input().split())
    idxn = n-1
    idxm = m-1
    cup[idxn], cup[idxm] = cup[idxm], cup[idxn]

for j in range(3):
    if cup[j] == 1:
        print(j+1)
