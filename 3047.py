i = []
i = list(input().split())
ABC = str(input())
LABC = list(ABC)
answer = []
for k in range(3):
    i[k] = int(i[k])
if max(LABC) == LABC[0]:
    if min(LABC) == LABC[2]:
        answer.append(max(i))
        i.remove(max(i))
        answer.append(max(i))
        answer.append(min(i))
    elif min(LABC) == LABC[1]:
        answer.append(max(i))
        answer.append(min(i))
        i.remove(max(i))
        answer.append(max(i))
elif max(LABC) == LABC[1]:
    if min(LABC) == LABC[2]:
        temp = (max(i))
        i.remove(max(i))
        answer.append(max(i))
        answer.append(temp)
        answer.append(min(i))
    elif min(LABC) == LABC[0]:
        answer.append(min(i))
        answer.append(max(i))
        i.remove(max(i))
        answer.append(max(i))
elif max(LABC) == LABC[2]:
    if min(LABC) == LABC[0]:
        answer.append(min(i))
        temp = (max(i))
        i.remove(max(i))
        answer.append(max(i))
        answer.append(temp)
    elif min(LABC) == LABC[1]:
        temp = (max(i))
        i.remove(max(i))
        answer.append(max(i))
        answer.append(min(i))
        answer.append(temp)

for j in range(3):
    print(answer[j],end=' ')