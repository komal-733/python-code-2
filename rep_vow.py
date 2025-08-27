def rep_vow(s,c):
  v="AEIOUaeiou"
  for i in v:
      s=s.replace(i,c)
  return s
print(rep_vow("the aardvark", "#"))