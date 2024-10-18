def last_day_number(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

def judge_day(m,d):
    if m <= 12 and last_day_number(m) >= d:
        return True
    return False

m,d = map(int, input().split())

if judge_day(m,d):
    print("Yes")
else:
    print("No")