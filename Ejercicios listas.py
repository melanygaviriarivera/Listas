
# 1
"""

a=str(input("Ingrese un elemento de la lista (# para terminar):\n"))
l=[""]
while (a!="#"):
  l.append(a)
  a=str(input("Ingrese un elemento de la lista (# para terminar):\n"))
l.remove("")
print("La lista es:", l)

for i in l:
  if (l.count(i)>1):
    l.remove(i)
print("Sin elementos repetidos:\n", l)

"""# 2"""

a=str(input("Ingrese un elemento de la lista 1 (# para terminar):\n"))
l1=[""]
while (a!="#"):
  l1.append(a)
  a=str(input("Ingrese un elemento de la lista 1 (# para terminar):\n"))
l1.remove("")
print("La lista 1 quedó:", l1, "\n")

a=str(input("Ingrese un elemento de la lista 2 (# para terminar):\n"))
l2=[""]
while (a!="#"):
  l2.append(a)
  a=str(input("Ingrese un elemento de la lista 2 (# para terminar):\n"))
l2.remove("")
print("La lista 2 quedó:", l2)

#Lista de palabras que aparecen en las dos listas
rep=[]
#Lista de palabras que aparecen en la primera pero no en la segunda
pri=[]
#Lista de palabras que aparecen en la segunda pero no en la primera
seg=[]
#lista de palabras que aparecen en ambas listas
rep=[]

for a in l1:
  if a in l2:
    rep.append(a)
  else:
    pri.append(a)

for a in l2:
  if not a in l1:
    seg.append(a)

print("1. Lista de palabras que aparecen en las dos listas:\n", rep)
print("2. Lista de palabras que aparecen en la primera pero no en la segunda:\n", pri)
print("3. Lista de palabras que aparecen en la segunda pero no en la primera:\n", seg)
print("4. Lista de palabras que aparecen en ambas listas:\n", rep)