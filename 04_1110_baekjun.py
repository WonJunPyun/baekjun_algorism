plus = int(input())
cycle = plus
count = 0

while True :
    a = cycle//10  # 2
    b = cycle% 10 # 6
    c = (a + b) % 10 # 8
    cycle = (b * 10) + c

    count = count +1
    if (cycle == plus):
        break
print(count)








