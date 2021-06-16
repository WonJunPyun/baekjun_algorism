a, b, v = map(int, input().split())
day= 0
#a 올라가는시간 / b 떨어짐 / v 나무 높이
if (v-b) % (a-b) != 0 :
    day = (v-b)//(a-b) +1
else:
    day = (v-b)//(a-b)

print(day)


