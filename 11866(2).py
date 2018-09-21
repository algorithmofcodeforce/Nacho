n, m = map(int, input().split())
list = [i for i in range(1,n+1)]
ans = [0]*n
index = 0
delete = m-1

while len(list) != 0:
    while delete >= len(list):
        delete = delete - len(list)
    ans[index] = list[delete]
    del list[delete]
    delete = delete + (m - 1)
    index += 1


print("<", end = "")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end = ">")
    else:
        print(ans[i], end =", ")