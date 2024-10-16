def is_prime(x):
    for i in range(2,x):
        if i == 1:
            return False
        if x % i == 0:
            return False
    return x

a, b = map(int, input().split())

prime_list = []

for i in range(a, b+1):
    if is_prime(i):
        prime_list.append(i)
    
print(sum(prime_list))