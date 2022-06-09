lista1 = ["a","b","c"]
lista2 = ["c","b","e"]

count=0
for x in lista1:
    for y in lista2:
        if x==y:
            count +=1
            
print("Parecidas") if count > 1 else print("No coinciden")