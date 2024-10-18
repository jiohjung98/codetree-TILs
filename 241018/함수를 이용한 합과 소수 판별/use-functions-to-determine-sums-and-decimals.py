def prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def even_num(x):
    a = x // 10
    b = x % 10
    if (a+b) % 2 == 0:
        return True
    else:
        return False

x, y = map(int, input().split())

cnt = 0
for i in range(x,y+1):
    if prime_num(i) and even_num(i):
        cnt += 1

print(cnt)