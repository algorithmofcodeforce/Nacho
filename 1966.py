t = int(input())
ans = [0] * t
for i in range(t):
    n,index = (map(int, input().split()))
    mon = list(map(int, input().split()))
    temp = 0
    maxtemp = 0
    this = 0
    if index >=  n:
        index = n-1
    for j in range(10000):
        maxtemp = max(mon)
        if mon[0] < maxtemp:
            temp = mon[0]
            del mon[0]
            mon.append(temp)
            if index == 0:
                index = index + len(mon)-1
            else:
                index -= 1
        elif mon[0] == maxtemp:
            if index > 0:
                del mon[0]
                index -= 1
                this += 1
            elif index == 0:
                this += 1
                ans[i] = this
                break
for i in range(len(ans)):
    print(ans[i])