#Variável
name = 'Harry'
#Lista
names = ['Harry', 'Barry', 'Giovanni', 'George']

#Lista
list = [1, 2, 3, 4, 5]

#Tupla
tupla = (10.0, 20.0) #coordenada, por exemplo

print(name[2])
print(names[2])
print(list[2])

#Imprime a lista inteira
print(names)

#Adiciona um valor ao fim da lista
#names.append = 'Draco'

#print(names)

#Ordena a lista
names.sort()

print(names)



#Set
s = set()

#Add elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
#Sets só mostram uma vez, ou seja, contanto que apareça ele já adiciona
s.add(3)

#Printa o set
print(s)

s.remove(2)

print(s)
print(f"The set has {len(s)} elements")




#Dicionario
houses = {
    "Harry": "Gryffindor", 
    "Draco": "Slytherin"
}

houses["Hermione"] = "Gryffindor"

print(houses["Harry"])