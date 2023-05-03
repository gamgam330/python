import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = set(sys.stdin.readline().rstrip().split()[1:])
cnt = 0

part_list = []
F_list = []

for _ in range(m):
    part_list.append(set(sys.stdin.readline().rstrip().split()[1:]))
    F_list.append(1)

for _ in range(m):
    for i, party in enumerate(part_list):
        if P.intersection(party):
            F_list[i] = 0
            P = P.union(party)

print(sum(F_list))