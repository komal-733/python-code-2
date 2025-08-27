def cor_sign(s):
  try: 
    return(eval(s))
  except:
    return False

s="13 < 44 > 33 <1"
print(cor_sign(s))
