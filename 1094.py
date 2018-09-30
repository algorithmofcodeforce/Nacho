domak = [64,32,16,8,4,2,1]
X = int(input())
amount = 0
cm = 64
i = 1
answer = 0
for i in list(domak):
    if amount + i <= X:
        amount += i
        answer += 1
print(answer)
