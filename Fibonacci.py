#Segunda questão

n = int(input("Qual o numero?"))

a0 = 0
a1 = 1

if n == 0:
  print(0)
elif n <= 2:
  print(1)
else:
  for i in range(0,n-1):
    a3 = a0 + a1
    a0 = a1
    a1 = a3
  print("O",n, "elemento da sequencia é",a3)
