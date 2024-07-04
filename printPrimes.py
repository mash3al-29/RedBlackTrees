from typing import List

primes: list[int] = [2]
current: int = 3
while True:
    isPrime: bool = True
    for prime in primes:
        if current % prime == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(current)
    if current%10000 == 0:
        print(f"{(len(primes) / current) * 100}% are primes till {current}")
    current += 1
