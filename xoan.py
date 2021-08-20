import turtle
import math
t = turtle.Turtle()
i = int(input("Nhập khoảng cách dừng lại: "))
d = 0
while True:
  d+=1
  t.forward(d)
  t.right(40)
  c = t.position()
  x = c[0]
  y = c[1]
  st = (x*x) + (y*y)
  s = math.sqrt(st)
  print(s)
  if s > i:
      break
turtle.done()