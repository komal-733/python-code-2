import math
def cone_vol(h,r):
  if r==0:
    return 0
  return round(1/3*math.pi*(r**2)*h,2)

print(cone_vol(3,2))