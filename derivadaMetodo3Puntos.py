import math

def f(x):
  return x*math.exp(x)

def df(x):
  return math.exp(x)+x*math.exp(x)

def formula(x,h):
  return (0.5/h) * (-3*f(x)+ 4 * f(x+h) - f(x+(2*h))) + ((h**2)/3)

print("f'(2) directa = ",df(2),end="\n\n")
for x in range(1,5):
  a = formula(2,0.1**x)
  print("f'(",2+0.1**x,")",a, "Error: ", abs(a-df(2)))
