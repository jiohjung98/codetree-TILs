def perfect_num(x):
    if x % 2 == 0:
        return False
    elif x % 10 == 5:
        return False
    elif x % 3 == 0 and x % 9 != 0:
        return False
    else:
        return True


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if perfect_num(i) == True:
        cnt += 1

print(cnt)