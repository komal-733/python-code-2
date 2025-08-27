def binary(n):
  bstr=""
  while n>0:
    b = n%2 
    bstr = str(b) + bstr
    n=n//2
    
  return bstr if bstr else 0
print(binary(10))