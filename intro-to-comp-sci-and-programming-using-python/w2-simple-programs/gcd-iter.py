def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = a if a < b else b
    while a % gcd != 0 and b % gcd != 0:
        gcd -= 1

    return gcd

print(gcdIter(2, 12)) # 2