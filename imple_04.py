s = list(input())
num = 0
result = []
s.sort()

for i in s:
  if ord(i) >= 65:
    result.append(i)
    continue
  else:
    i = int(i)
    num += i
    
result.append(num)

for i in result:
  print(i, end='')