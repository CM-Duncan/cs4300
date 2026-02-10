def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_ten_primes():
    primes = []
    num = 2
    while len(primes) < 10:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def sum_one_to_hundred():
    total = 0
    n = 1
    while n <= 100:
        total += n
        n += 1
    return total
