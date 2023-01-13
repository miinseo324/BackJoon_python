N=int(input(""))
# N : 회의 수
time=[[0]*2 for _ in range(N)]

for i in range(N):
    start,end=map(int, input("").split( ))
    time[i][0]=start
    time[i][1]=end

time.sort(key=lambda x : (x[1], x[0]))
count=0
j=0
k=0
for i in range(N-1):
    if time[j][1]<=time[k+1][0]:
        count+=1
        j=i+1
        k=i+1
    else:
        k+=1
count+=1
print(count)
