def add(x,y):
    print(x,'+',y, '=', x+y);

def sub(x,y):
    print(x,'-',y, '=', x-y);

def mul(x,y):
    print(x,'*',y, '=', x*y);

def div(x,y):
    print(x,'/',y, '=', x//y);

input_nums = list(map(str, input().split()))

if input_nums[1] == '+':
    add(int(input_nums[0]), int(input_nums[2]))
elif input_nums[1] == '-':
    sub(int(input_nums[0]), int(input_nums[2]))
elif input_nums[1] == '*':
    mul(int(input_nums[0]), int(input_nums[2]))
else:
    div(int(input_nums[0]), int(input_nums[2]))