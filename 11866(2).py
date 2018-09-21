n, m = map(int, input().split()) #n과 m 값 받아오기
list = [i for i in range(1,n+1)] # 1부터n까지의 범위의 리스트 가져오기
ans = [0]*n #답을 넣을 칸 만들어두기
index = 0 #몇번째 값인지 가르키기용 (0부터 시작)
delete = m-1 #몇번째 인덱스 값을 지울지 정하기 (인덱스 값은 0부터 n-1까지기 때문에 -1)

while len(list) != 0: #범위를 정해준 리스트가 빌때까지 계속 반복
    while delete >= len(list): #만약 가르키는 값이 n의 값보다 길때 아래를 실행
        delete = delete - len(list) #
    ans[index] = list[delete] #ans의 index번째 값(처음은 0)을 list의 delete번째 값으로 바꿈
    del list[delete] #바꿔진 그 값은 제거
    delete = delete + (m - 1) #다음 식을 위해 del에 m-1을 더함
    index += 1 #다음 인덱스 값을 가리키기 위해 1을 더함


print("<", end = "")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end = ">")
    else:
        print(ans[i], end =", ")