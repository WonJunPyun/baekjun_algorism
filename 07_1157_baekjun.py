# upper() 소문자를 대문자로 바꾸어 줍니다
# lower() 대문자를 소문자로 바꾸어 줍니다 

Q = input().upper()
alphabet = []

for i in range(ord('A'),ord('Z')+1):
    alphabet.append(Q.count(chr(i)))

if alphabet.count(max(alphabet)) == 1:
    print(chr(alphabet.index(max(alphabet))+ord('A')))
else:
    print('?')