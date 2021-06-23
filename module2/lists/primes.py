#primes upto whatever range you want

primes = []

for num in range(2, 100):
    div_count = 0
    for div_by in range(1, num):
        if num % div_by == 0:
            div_count += 1
    if div_count == 0:
        primes.append(num)

print(primes)