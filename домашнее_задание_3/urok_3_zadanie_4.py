def myfunc(x, y):
  try:
      x=float(x)
      y= int(y)
  except ValueError:
      print('Программа работает только с  действительными x и целыми  y')
      return
  if x<=0 or y>= 0:
      print('Программа работае  только с положительными x и отрицательными y')
      return
  return x ** y

print(round(myfunc(5,-1),10))