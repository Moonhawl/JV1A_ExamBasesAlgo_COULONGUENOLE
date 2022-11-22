#Partie 1 - Tri à bulles

#1 - Écrire un programme permettant de permuter deux valeurs du tableau myTable :

myTable = [4,6,3,7,1,2]
stock = 0
print(myTable)

stock = myTable[2]
myTable[2]=myTable[1]
myTable[1]=stock

print(myTable)

#2 - Écrire un programme permettant le parcours du tableau au cours d’une itération du tri à
# bulles. On pourra se servir de la permutation définie dans l’exercice précédent.

myTable = [4,6,3,7,1,2]
pgv = myTable[0]

print(myTable)
print(pgv)

for i in range(len(myTable)):
    for j in range(i,len(myTable)):
        if myTable[j]>myTable[i] :
            if pgv<myTable[j]:
                pgv = myTable[j]
                
            
myTable.append(pgv)
myTable.pop(3)
    
print(myTable)
print(pgv)

#3/ Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
# un tableau grâce à l’algorithme du tri à bulles

myTable = [4,6,3,7,1,2]

for j in range(len(myTable)):
    ppv=myTable[j]
    ccp=j
    for i in range(j,len(myTable)):
        if (ppv>myTable[i]):
            ppv = myTable[i]
            ccp=i
    stock=myTable[j]
    myTable[j]=myTable[ccp]
    myTable[ccp]=stock
  
print(myTable)


#4/ Le tri à bulles est considéré comme très lent. Pourquoi ? Peut-on avoir une idée du temps
# nécessaire à son exécution, estimer son ordre de grandeur ?

#- Le tri à bulles est considéré comme très lent car pour l'effectuer, il faut que la machine analyse chacune
# des valeurs de chaque tableau.
# Le temps nécessaire à son execution se mesure probablement en centièmes de secondes.



