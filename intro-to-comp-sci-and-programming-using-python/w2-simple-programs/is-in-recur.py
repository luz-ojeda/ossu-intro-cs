def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    lenStr = len(aStr)
    if lenStr == 1 and aStr != char:
        return False

    middle = lenStr // 2
    
    if aStr[middle] == char:
        return True
    elif aStr[middle] > char:
        return isIn(char, aStr[:middle])
    else:
        return isIn(char, aStr[middle:lenStr])

# Basic Functionality
print(isIn('e', 'abcdef'))  # Expected Output: True
print(isIn('g', 'abcdef'))  # Expected Output: False

# Edge Cases
print(isIn('a', 'a'))       # Expected Output: True
print(isIn('b', 'a'))       # Expected Output: False
print(isIn('a', 'abc'))     # Expected Output: True
print(isIn('c', 'abc'))     # Expected Output: True

