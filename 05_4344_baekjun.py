a =  int(input())

for i in range(a):
    n = list(map(int, input().split()))
    average = sum(n[1:])/n[0]
    count = 0
    for a in n[1:]:
        if a > average:
            count += 1  
    result = count/n[0] *100
    print(f'{result:.3f}%')
