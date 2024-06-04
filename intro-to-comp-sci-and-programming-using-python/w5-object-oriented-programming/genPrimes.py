def genPrimes():
    """
    returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
    """
    last = 1
    primes = []
    
    while True:
        last += 1
   
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
        
