def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for idx, value in enumerate(aTup):
        if idx % 2 == 0:
            newTup = newTup + (value,)
            
    return newTup

print(oddTuples((1,2,3,4,5, 6, 7, 8, 9))) # (1, 3, 5, 7, 9)
        
