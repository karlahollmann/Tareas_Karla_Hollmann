import numpy as np
import vector as v

print("Vector a: ")
a=v.vectorcartesiano(1.5,0,2.4)
print("Vector cartesiano a = ", end='')
a.print()

print("\n")
print("Vector b: ")
b=v.vectorcartesiano(0,1,9)
print("Vector cartesiano b = ",end=' ')
b.print()

print("\n")
print("Vector c: ")
c=v.vectorcartesiano(4.2,0.05,0)
print("Vector cartesiano c = ",end=' ')
c.print()
print("\n")

class tranesfericas(v.vectorcartesiano):
    
    def __init__(self,x,y,z,r=0,t=0,p=0):
        v.vectorcartesiano.__init__(self,x,y,z)
        self.r=r
        self.t=t
        self.p=p
        
        mpp=np.sqrt(self.r**2+self.t**2+self.p**2)
        print("magnitud del vector esferico:",mpp)
        
    def tran(self):
        return tranesfericas(0,0,0,np.sqrt((self.x**2)+(self.y**2)+(self.z**2)),np.arccos((self.z)/np.sqrt((self.x**2)+(self.y**2)+(self.z**2))),np.arctan(self.y/self.x))

    def print(self):
        fe=[]
        fe.append(self.r)
        fe.append(self.t)
        fe.append(self.p)
        print(fe)

        
print("\n")    
print("Definimos los vectores a,b,c para la transformacion de coordenadas y realizamos la transformación \n")

print("Vector a: ")
a2=tranesfericas(1.5,0,2.4,0,0,0)
print("\n")
print("Transformacion coordenadas esfericas")
a3=a2.tran()
print("vector esferico a=", end='')
a3.print()

print("\n")

print("Vector b: ")
b2=tranesfericas(1e-20,1,9,0,0,0)
print("\n")
print("Transformacion coordenadas esfericas")
b3=b2.tran()
print("vector esferico b=", end='')
b3.print()

print("\n")

print("Vector c: ")
c2=tranesfericas(4.2,0.05,0,0,0,0)
print("\n")
print("Transformacion coordenadas esfericas")
c3=c2.tran()
print("vector esferico c=", end='')
c3.print()
print("\n") 

print("\n")        
print("Producto punto vectores cartesianos \n")

print("a*b = ",end='')
a.prodpunto(b)


print("\n")
print("a*c = ",end='')
a.prodpunto(c)



print("\n")
print("b*c = ",end='')
b.prodpunto(c)
print("\n") 

print("\n")        
print("Producto cruz vectores cartesianos \n")

pca=v.prodcruz(1.5,0,2.4)
pcb=v.prodcruz(0,1,9)
pcc=v.prodcruz(4.2,0.05,0)

print("\n")
print("axb:")
r1=pca.cruz(pcb)
print("axb = ", end='')
r1.print()

print("\n")
print("axc:")
r2=pca.cruz(pcc)
print("axc = ", end='')
r2.print()

print("\n")
print("bxc:")
r3=pca.cruz(pcc)
print("bxc = ", end='')
r3.print()
print("\n") 

print("\n")  
print("angulos entre vectores \n")

print("angulo entre a y b")
a.ang(b)

print("\n") 
print("angulo entre a y c")
a.ang(c)
        
print("\n") 
print("angulo entre b y c")
b.ang(c)
