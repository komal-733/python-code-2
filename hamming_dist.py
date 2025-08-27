def hamming_dist(s1,s2):
  count=0
  if len(s1)!=len(s2):
    raise ValueError("Both String should have equal strength")
  
  for i in range(len(s1)) :
    if s1[i]!=s2[i]:
       count+=1
       
  return count

s1= "abcbba"
s2= "abcbde"
print(hamming_dist(s1,s2))