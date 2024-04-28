import math

def calc_polygon_area(n, s):
    num = 0.25 * n * (s**2)
    den = math.tan(math.pi/n)
    
    return num/den

def polysum(n, s):
    area = calc_polygon_area(n, s)
    perimeter = (n*s)**2
    
    return area + perimeter

print(round(polysum(100, 2), 4))