def yun_year(x):
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 != 0:
            return 'false'
        else:
            return 'true'
    return 'false'

y = int(input())
print(yun_year(y))