sanggen = int(input())

s_express = 0
while sanggen >= 0:
    if sanggen % 5 == 0:
        s_express += (sanggen//5)
        print(s_express)
        break
    sanggen -= 3
    s_express += 1
else :
    print(-1)