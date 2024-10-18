n1, n2 = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sum_a = ''
for a in a_list:
    sum_a += str(a)

sum_b = ''
for b in b_list:
    sum_b += str(b)

if sum_b in sum_a:
    print("Yes")
else:
    print("No")