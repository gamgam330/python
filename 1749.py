import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
result = -1000000000

for i in range(n):
    arr.append(list(map(int, input().split())))

sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = sum[i][j-1] + arr[i-1][j-1] + sum[i-1][j] - sum[i-1][j-1]

for a in range(1, n+1):
    for b in range(1, m+1):
        for x in range(a, n+1):
            for y in range(b, m+1):
                result = max(result, sum[x][y] - sum[a-1][y] - sum[x][b-1] + sum[a-1][b-1])

print(result)