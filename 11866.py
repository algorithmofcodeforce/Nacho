n, m = (input("범위, n번째 사람")).split()
print("범위:",n,"단위:",m)
intn = int(n)
intm = int(m)
numbersample = list(range(1, intn+1))
suyeol = []
for i in range(intn):
    for j in range(1,intn+1):
        suyeol.append(j)
print(suyeol)
prelist = [1,1,0,1,1,0,1,1,0]

#리스트 인덱스값 삭제 연습
'''
for i in range(2,len(prelist)-1,2):
    del prelist[i]
    print("삭제",i,prelist)'''