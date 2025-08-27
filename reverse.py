def reverse(s):
  if type(s)==bool:
    return not s
  else:
    return "boolean expected"
  
  
print(reverse(True))