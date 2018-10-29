m, n = map(int, input().split())
num = input().split()
for j in range(len(num)):
    num[j] = int(num[j])

num.sort()

def egin(O, upper, lower):
    mid = (upper + lower) // 2
    if num[mid] == O:
        return int(mid)
    elif num[mid] > O:
        return int(egin(O, mid, lower))
    elif num[mid] < O:
        return int(egin(O, upper, mid))

if n <= 0:
    print(1)
else:
    print(egin(n, len(num), 0) + 1)




