n = int(input())

directions = list(input().split())
direction = ['R', 'L', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
x, y = 1, 1

for i in directions:
  for j in range(4):
    if direction[j] == i:
      nx = x + dx[j]
      ny = y + dy[j]
      if nx <= 0 or ny <= 0 or nx > n or ny > n:
        break
      x, y = nx, ny

print(x, y) 