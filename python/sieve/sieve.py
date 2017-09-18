def sieve(interval):
    primes = []

    if interval > 1:
        primes = list(range(2, interval + 1))
        i = 0
        while i < len(primes):
            j = i + 1
            primeNumber = primes[i]
            while j < len(primes):
                if primes[j] % primeNumber == 0:
                    primes.remove(primes[j])
                else:
                    j += 1
                    
            i += 1

    return primes
