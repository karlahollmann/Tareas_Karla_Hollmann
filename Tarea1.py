
import funciones as f

archivo=open("Pascal-n.txt","w")
archivo.write("Triangulo de Pascal \n")
archivo.write(str(f.pascal(4)))
archivo.close()

def probabilidad(n,k): #n lanzamientos, numero k de veces que cae cara/sello
    return f.binomial(n,k)/(2**n)

print("""si se realiza el experimento 100 veces, la probabilidad 
de que el resultado sean 10 veces cara es:""", probabilidad(100,10),"\n")


print("""si se realiza el experimento 100 veces, la probabilidad 
de que el resultado sean 30 veces cara es:""", probabilidad(100,30),"\n")

#caiga mas de 30 veces cara
print("""si se realiza el experimento 100 veces, la probabilidad 
de que el resultado sean 50 veces cara es:""", probabilidad(100,50),"\n")
