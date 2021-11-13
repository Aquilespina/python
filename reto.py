# TODO: Desarrollar un programa que calcule la distancia, o la velocidad o el tiempo recorrido por un auto a Vc EV = 2

# dependiendo de lo que el usuario quiera (Aquiles)

# Tips: si el usuario quiere el tiempo, deberas leer la distancia y la velocidad

# Formula: D = V*T , V = D/T, T = D/V    D(m),T(s),V(m/s)

# input: 10 * 2 D

# output: La distancia recorrida es de 20 metros
x=int(input("""Digite las opciones que desee encontrar 
      [1]La distancia 
      [2]La velocidad
      [3]El tiempo
      """))
if x==1:
    print("-----Valor a obtener Distancia --------")
    tiempo=float(input("Digite el tiempo : "))
    velocidad=float(input("Digite la velocidad: "))
    distancia =(velocidad * tiempo)
    print(f"La distancia recorrida es de {distancia} metros ")
elif x==2:
    print("-----Valor a obtener Velocidad --------")
    distancia=float(input("Digite la distancia : "))
    tiempo=float(input("Digite el tiempo: "))
    velocidad=(distancia/tiempo)
    print(f"La velodidad calculada es {velocidad} m/s")
    
    
else :
    print("-----Valor a obtener Tiempo --------")
    distancia=float(input("Digite la distancia : "))
    velocidad=float(input("Digite la velocidad: "))
    tiempo=(distancia/velocidad)
    print(f"El tiempo es {tiempo} s")

