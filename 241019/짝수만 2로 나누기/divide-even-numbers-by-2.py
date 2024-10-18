n = int(input())
nums = list(map(int, input().split()))

def half_num(x):
    for i in range(n):
        if x[i] % 2 == 0:
            x[i] //= 2

half_num(nums)

for x in nums:
    print(x, end=' ')