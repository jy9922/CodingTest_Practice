directions = [(2,-1),(2, 1),(-2, 1),(-2,-1),(1, 2),(-1, 2), (1, -2), (-1, -2)]

x, y = input()
x = ord(x) - 96
y = int(y)
count = 0

for i in range(8):
  nx = x + directions[i][0]
  ny = y + directions[i][1]
  if nx <= 0 or ny <= 0 or nx >= 9 or ny >= 9:
    continue
  count += 1

print(count)

  