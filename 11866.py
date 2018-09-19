n, m = (input("범위, n번째 사람")).split()
print("범위:",n,"단위:",m)

intn = int(n)
intm = int(m)
numbersample = list(range(1, intn+1))
suyeol = []
josephus = []
count = 1

for i in range (intn):
    for j in range(1,intn+1):
        suyeol.append(j)

print(suyeol)
for i in range (intm-1, len(suyeol),intm):
    if count <= intn:
        josephus.append(suyeol[i])
        count += 1
        print(i,josephus)

#리스트 인덱스값 삭제 연습
'''
prelist = [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0]
prelistwo = []
for i in range(2,len(prelist)-1,3):
    prelistwo.append(prelist[i])
    print("추가",i,prelistwo)
'''