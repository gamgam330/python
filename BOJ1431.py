import sys
input = sys.stdin.readline

def func(input):
    result = 0
    for i in input:
        if i.isdigit():
            result += int(i)
    return result

arr = [input() for _ in range(int(input()))]

arr.sort(key = lambda x:(len(x), func(x), x))

for i in arr:
    print(i)