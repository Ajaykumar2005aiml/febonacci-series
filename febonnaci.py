n=int(input("enter a number to print febinocci till that:"))
a=0
b=1
if n>1:
  print(a)
  print(b)
  for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
else:
  print(a)
