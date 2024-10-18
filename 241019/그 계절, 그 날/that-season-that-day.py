def day_calc(x, y):
    # 윤년 계산 수정
    if y == 2:
        if (x % 400 == 0) or (x % 100 != 0 and x % 4 == 0):
            return 29  # 윤년일 경우 2월은 29일
        else:
            return 28  # 윤년이 아닐 경우 2월은 28일
    if y in [4, 6, 9, 11]:
        return 30  # 4, 6, 9, 11월은 30일
    else:
        return 31  # 그 외의 달은 31일

def season_calc(x, y, z):
    maxDay = day_calc(x, y)
    if z > maxDay:  # 입력된 일이 그 달의 최대 일수를 넘으면 잘못된 입력
        print(-1)
    else:
        if 1 <= y <= 3:  # 1월 ~ 3월은 겨울
            print('Winter')
        elif 4 <= y <= 6:  # 4월 ~ 6월은 봄
            print('Spring')
        elif 7 <= y <= 9:  # 7월 ~ 9월은 여름
            print('Summer')
        else:  # 10월 ~ 12월은 가을
            print('Fall')

# 입력을 받습니다.
y, m, d = map(int, input().split())

# 계절 계산 함수 호출
season_calc(y, m, d)