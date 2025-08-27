def evenly_div(a,b,c):
  num=0
  for i in range(a,b+1):
    if i%c==0:
      num+=i
      
  return num

print(evenly_div(1,10,5))