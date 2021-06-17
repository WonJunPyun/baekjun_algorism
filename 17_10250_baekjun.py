n = int(input())

# h 호텔의층수  , w 각층 방의수 , n 몇번째 손님

for i in range(n):
    h,w,n = map(int,input().split())
    a = n%h
    b = n/h+1
    if a== 0:
        a = h
        b -= 1
    print(a*100+b)
