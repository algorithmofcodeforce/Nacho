Count = int(input())
i = []
i = list(input().split())

for k in range(1,Count):
    gcd = []
    for j in range(1,int(i[k])+1):
        if int(i[0]) % j == 0 and int(i[k]) % j == 0:
            gcd.append(int(j))

    num = int(max(gcd))
    x = str(int(i[0]) // num)
    y = str(int(i[k]) // num)
    print(x+"/"+y)