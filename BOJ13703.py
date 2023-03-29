DEPTHMAX = 63 * 2 + 1
MAX = 63 + 1

cache = [[-1 for j in range(MAX)] for i in range(DEPTHMAX)]

def isAlive(depth, seconds):
    if depth == 0:
        return 0
    elif seconds == 0:
        return 1

    result = cache[depth][seconds]
    if result != -1:
        return result

    result = isAlive(depth + 1, seconds - 1) + isAlive(depth - 1, seconds - 1)
    cache[depth][seconds] = result
    return result

if __name__ == "__main__":
    k, n = map(int, input().split())

    print(isAlive(k, n))