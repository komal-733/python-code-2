def move_to_end(l,n):
  nlist=[]
  
  for i in l:
    if i == n:
      continue
    nlist.append(i)
    
  length= l.count(n)
  
  nlist += [n]*length
  return nlist

l=["a", "a", "a", "b"]
n="a"
print(move_to_end(l,n))