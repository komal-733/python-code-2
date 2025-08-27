def curzon(n):
  return (2**n+1) % (n*2+1) == 0

print(curzon(10))