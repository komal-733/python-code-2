def filter_list(l):
  nlist=[]
  nlist=[i for i in l if isinstance(i,int)]
  return nlist

l=["A", 0, "Edabit", 1729, "Python", 1729]
print(filter_list(l))