n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for e in arr:
    print(e, end=' ')