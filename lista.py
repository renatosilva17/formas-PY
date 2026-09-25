#contador = 0
#limite = len(notas) - 1

#while contador <= limite:
#print (f"sua nota é: {notas[contador]}")
# contador += 1

notas = {7.0, 1.5, 10.0, 8.5, 3.0}
notas.add(9.0)
notas.add(5.5)
notas.remove(5.5)
notas.remove(9.0)

#para adicionar uma nova nota (notas.append(7.7))
#para remover uma nota (notas.pop(se n colocar nada ele exclui o ultimo))
#para modificar uma nota (notas[2] = 0.0)



for nota in notas:
  print(f"sua nota é: {nota}")