import random
#Exercice 2
n = int(input("Entrer un entier n: "))
result = 2 ** n
print("Le résultat de la multiplication de 2 par lui-même", n, "fois est:", result)

#Exercice 3
def passage(moyenne):
    if (moyenne < 8):
        return "RECALE"
    elif (8 <= moyenne and moyenne < 10):
        return "Oral rattrappage"
    elif (10 <= moyenne and moyenne < 12):
        return "admis"
    elif (12 <= moyenne and moyenne < 14):
        return "ASSEZ BIEN"
    elif (14 <= moyenne and moyenne < 16):
        return "bien"
    elif (moyenne >= 16):
        return "très bien"

#Exercice 4.1
def bissextile(annee):
    if (annee%4 == 0 and (annee%100 != 0 or annee%400 == 0)):
        return True;
    return False;
print(bissextile(2000))

#Exercice 4.2
def nbJoursAnnee(annee):
    if (bissextile(annee)):
        return 365;        
    else :
        return 364;
print(bissextile(2000))
    
#Exercice 4.3
def nbJourMois(annee, mois):
    if (mois == 1): 
        return 31;
    elif (mois == 2): 
        if (bissextile(annee)):
            return 29;
        else:
            return 28;
    elif (mois == 3): 
        return 31;
    elif (mois == 4): 
        return 30;
    elif (mois == 5): 
        return 31;
    elif (mois == 6): 
        return 30;
    elif (mois == 7): 
        return 31;
    elif (mois == 8): 
        return 31;
    elif (mois == 9): 
        return 30;
    elif (mois == 10): 
        return 31;
    elif (mois == 11): 
        return 30;
    else: 
        return 31; 
print(bissextile(2000))
    
#Exercice 5
def entier(n):
    startN = n
    maxN = 0;
    etape = 0;
    while (n > 1):
        if (n%2 == 0):
            n = n / 2;
        else:
            n = (n * 3) + 1
        etape += 1
        if (n > maxN):
            maxN=n;
        # print(f"number get : {n}")
    print(f"Pour n = {startN} => maxN : {maxN}, etape : {etape}")

for i in range(1, 21):
    entier(i)

#Exercice 6
list = [13, 23, 33, 43]
listRandom = []
for i in range(100):
    listRandom.append(random.randrange(1, 1000))

listRandomImpaire = [val for val in listRandom if val%2 != 0]
print(listRandomImpaire)

#Exercice 7
def somme(list):
    sommeTotal = 0
    for element in list:
        sommeTotal += element
        # print(element)
    return sommeTotal

print (somme(listRandomImpaire))

#Exercice 8
def max(list):
    max = 0;
    for element in list:
        if (element > max):
            max = element
    return max
    

