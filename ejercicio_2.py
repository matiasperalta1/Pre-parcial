# persona = {clave,valor}
persona = {}

c = True

while c:
    clave = input("Dato a introducir: ")
    valor = input(clave + ": ")
    persona[clave]= valor
    print(persona)
    q = input("Quiere añadir un nuevo dato? si =1/ no=0")
    if q == 'si':
        c = False
        