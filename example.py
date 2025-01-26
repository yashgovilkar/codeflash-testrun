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

def slow_function():
    primes = []
    for i in range(1000):
        if is_prime(i):
            primes.append(i)
    return primes


def main():
    primes = slow_function()
    print(f"Found {len(primes)} primes up to 1000.")

if __name__ == "__main__":
    main()