def nums(x):
    y = []
    for i in str(x):
        y.append(int(i))
    if x % 2 == 0 and (y[0]+y[1]) % 5 == 0:
        return 'Yes'
    else:
        return 'No'

a = int(input())

print(nums(a))