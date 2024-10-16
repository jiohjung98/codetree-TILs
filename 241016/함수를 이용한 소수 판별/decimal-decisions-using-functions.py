def is_prime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return x

a, b = map(int, input().split())

prime_list = []

for i in range(a, b+1):
    if is_prime(i):
        prime_list.append(i)
    
print(sum(prime_list))