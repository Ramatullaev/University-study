# Write a Python program to calculate the area of regular polygon.

import math
# [L**2 * n]/[4*tan(180/n)] 
n = int(input())
l = float(input())
area = (l ** 2 * n)/(4*math.tan(math.pi/n))
print(int(area))