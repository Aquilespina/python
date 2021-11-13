nota1=float(input("Ingresa la nota 1 : "))
nota2=float(input("Ingresa la nota 2 : "))
nota3=float(input("Ingresa la nota 3 : "))
nota4=float(input("Ingresa la nota 4 : "))
nota5=float(input("Ingresa la nota 5 : "))
#---------Asinacio de las notas
prom=((nota1+nota2+nota3+nota4+nota5)/5)
print(prom)

if prom>=91:
    notal_letra="A"
    print(notal_letra)#Imprimir en otra funcion 
elif prom >=81:
    notal_letra="B"
elif prom >=71:
    notal_letra="C"
elif prom >= 61:
    notal_letra="D"
else:
    notal_letra="F"
    
    
