from collections import deque

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
visited = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = deque()
enter = []

for i in range(N):
    if maze[i][0] == '.':
        enter.append((i, 0))
    if maze[i][M-1] == '.':
        enter.append((i, M-1))

for j in range(M):
    if maze[0][j] == '.':
        enter.append((0, j))
    if maze[N-1][j] == '.':
        enter.append((N-1, j))

start = enter[0]
end = enter[1]

stack.append(start)
visited.add(start)

while stack:
    x, y = stack[-1]
    visited.add((x, y))
    blocked = True

    if (x, y) == end:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '.' and (nx, ny) not in visited:
            stack.append((nx, ny))
            blocked = False

    if blocked:
        maze[x][y] = '@'
        stack.pop()

for i in range(N):
    for j in range(M):
        if maze[i][j] == '.' and (i, j) not in visited:
            maze[i][j] = '@'

for row in maze:
    print(''.join(row))
