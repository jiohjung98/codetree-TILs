def sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result // 10

n = int(input())

print(sum(n))