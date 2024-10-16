# a이상 b이하
# 1. 3,6,9 중 하나가 들어있음
# 2. 숫자 자체가 3의 배수

def is_contain_369(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n //= 10
    return False

def is_number_369(n):
    return is_contain_369(n) or (n % 3 == 0)

cnt = 0
x,y = map(int, input().split())
for i in range(x,y+1):
    if is_contain_369(i):
        cnt += 1

print(cnt)