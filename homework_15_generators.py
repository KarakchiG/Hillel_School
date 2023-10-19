# First way
def generate_primes_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    for num, prime_num in enumerate(primes):
        if prime_num:
            yield num


lower_num = int(input("Enter lower num: "))
upper_num = int(input("Enter upper num: "))

if lower_num < 2:
    lower_num = 2

print(f"Prime numbers between {lower_num} and {upper_num}:")
for prime in generate_primes_eratosthenes(upper_num):
    if prime >= lower_num:
        print(prime)


# Second way
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num


print("Prime numbers in you range are: ")
for prime in prime_numbers(start=20, end=100):
    print(prime)
