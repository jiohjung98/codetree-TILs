n = int(input())
arr = []
for _ in range(n):
    x = input()
    if 'push_back' in x:
        k, y = x.split( )
        arr.append(int(y))
    elif 'get' in x:
        k, y = x.split( )
        print(arr[int(y)-1])
    elif x == 'size':
        print(len(arr))
    elif x == 'pop_back':
        arr.pop()