import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:x[1])

min = []
cnt = 0

for i in arr:
    while min and min[0] <= i[1]:
        heapq.heappop(min)
    heapq.heappush(min, i[2])
    cnt = max(cnt, len(min))

print(cnt)