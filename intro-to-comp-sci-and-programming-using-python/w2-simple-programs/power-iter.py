def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    power = base;
    for i in range(1, exp):
        power *= base
        
    return power

print(iterPower(3,3))