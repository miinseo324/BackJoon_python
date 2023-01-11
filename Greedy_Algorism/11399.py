member=int(input(""))
# member : 줄 서있는 사람의 수
min=list(map(int,input("").split(" ")))
# min : 리스트로 인출하는데 걸리는 시간을 저장함
min.sort()
sum=0
for i in min:
    sum += (i*member)
    member-=1
print(sum)
