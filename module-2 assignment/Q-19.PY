def not_poor(a):
  snot = a.find('not')
  spoor = a.find('poor')
  
  if spoor > snot and snot>0 and spoor>0:
    a = a.replace(a[snot:(spoor+4)], 'good')
    return a
  else:
    return a
print(not_poor(input("enter the string")))

