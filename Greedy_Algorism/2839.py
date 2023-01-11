N=int(input(""))
# N : 총 설탕 무게
# a : 5kg 설탕 봉지 개수
# b : 3kg 설탕 봉지 개수

if int(N%5) == 0:
        print(int(N/5))
        # N이 5로 떨어지면 그대로 출력
else:
    a=int(N/5)
    while 1:
        res=N-(a*5)
        if res%3==0:
            b=res/3
            print(int(a+b))
            break
        else:
            a-=1
            if a<0:
                print("-1")
                break
            
