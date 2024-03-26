#Quinta questão

s = str(input("Qual a string? "))
rev_s = ""

for i in range(len(s)-1, -1, -1):
  rev_s += s[i]

print("A string reversa é:",rev_s)