def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def slow_function():
    primes = []
    for i in range(1000):
        if is_prime(i):
            primes.append(i)
    return primes

def redundant_loop():
    data = [x**2 for x in range(10000)]
    total = 0
    for num in data:
        total += num
    average = total / len(data)
    return average

def main():
    primes = slow_function()
    print(f"Found {len(primes)} primes up to 1000.")
    avg = redundant_loop()
    print(f"Average of squares: {avg}")

if __name__ == "__main__":
    main()