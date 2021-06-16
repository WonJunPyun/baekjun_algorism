a, b = map(int, input().split())

def gcm(x, y):	# 최대공약수
    while y:	# 나머지가 0일 때 까지
        x, y = y, (x % y)	# 재귀
    return x

def lcm(x, y):	# 최소공배수
    result = (x * y) // gcm(x, y)	# x, y의 곱을 최대공약수로 나눠줌
    return result

print(gcm(a, b))
print(lcm(a, b))