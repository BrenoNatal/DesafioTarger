# DesafioTargert
1)
Resposta: SOMA = 13

2)

```
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
```
3)
a) 9
b) 128
c) 49
d) 100
e) 13
f) 200

4)
Ligo o primeiro interrupetor e espero um tempo depois de espera desligo ele e ligo o segundo interruptor e vou ate uma das salas e vejo se a lampada esta quente, se esta ligada ou se esta fria e apagada, caso esteja quente o primeiro interruptor conecta com essa sala ai é so ir em uma das outras salas para desocbrir os outros dois interruptores, e para os outros casos é o mesmo raciocinio.

5)

```
s = str(input("Qual a string? "))
rev_s = ""

for i in range(len(s)-1, -1, -1):  
  rev_s += s[i]

print("A string reversa é:",rev_s)
```
