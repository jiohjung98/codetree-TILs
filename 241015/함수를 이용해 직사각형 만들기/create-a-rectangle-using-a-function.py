def square(x,y):
    for _ in range(x):
        print('1' * y)

input_nums = list(map(int, input().split()))
square(input_nums[0], input_nums[1])