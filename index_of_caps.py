def index_of_caps(s):
  return[i for i in range(len(s)) if s[i].isupper()]

s="determine"
print(index_of_caps(s))