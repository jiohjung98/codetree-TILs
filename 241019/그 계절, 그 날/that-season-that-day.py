def day_calc(x,y):
    if y == 2:
        if x % 4 == 0:
            if (x % 400 == 0) or (x % 100 != 0 and x % 4 == 0):
                return 29  # 윤년일 경우 2월은 29일
            else:
                return 28  # 윤년이 아닐 경우 2월은 28일
    if y == 4 or y == 6 or y == 9 or y == 11:
        return 30
    else:
        return 31

def season_calc(x,y,z):
    maxDay = day_calc(x,y)
    if maxDay < z:
        print(-1)
    else:
        if 1 < y and y <= 3:
            print('Winter')
        elif 3 < y and y <= 6:
            print('Spring')
        elif 6 < y and y <= 9:
            print('Summer')
        else:
            print('Fall')

y, m, d = map(int, input().split())

season_calc(y,m,d)