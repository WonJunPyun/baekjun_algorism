a = int(input())
b = list(input())

result1 = a*int(b[2])
result2 = a*int(b[1])
result3 = a*int(b[0])
result4 = (result1 + (result2 * 10) + (result3*100))
print(result1,result2,result3,result4)