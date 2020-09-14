import numpy as np

class vectorcartesiano:
    
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
        
        m=np.sqrt(self.x**2+self.y**2+self.z**2)
        print("magnitud del vector cartesiano:",m)
        
    def prodpunto(self, other): 
        print((self.x*other.x)+(self.y*other.y)+(self.z*other.z))
    
    def __add__(self,other):
        return vectorcartesiano(self.x+other.x, self.y+other.y, self.z+other.z)
           
    def __sub__(self,other):        
        return vectorcartesiano(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __eq__(self, other):    
        return vectorcartesiano(self.x==other.x, self.y==other.y, self.z==other.z)
    
    def ang(self,other):
        magself=np.sqrt(self.x**2+self.y**2+self.z**2)
        magother=np.sqrt(other.x**2+other.y**2+other.z**2)
        prod=(self.x*other.x)+(self.y*other.y)+(self.z*other.z)
        print(np.arccos(prod/(magself*magother)))
    
    def __getitem__(self,item):
        f=[]
        f.append(self.x)
        f.append(self.y)
        f.append(self.z)
        return f[item-1]
        
    def print(self):
        print(f'[{self.x},{self.y},{self.z}]')
        
        
class prodcruz(vectorcartesiano):
    
    def __init__(self,x,y,z):
        vectorcartesiano.__init__(self,x,y,z)
    
    def cruz(self,other):
        return prodcruz((self.y*other.z)-(self.z*other.y),-((self.x*other.z)-(self.z*other.x)),(self.x*other.y)-(self.y*other.x))
    
    def print(self):
        print(f'[{self.x},{self.y},{self.z}]')
        
        
class vectorpolar(vectorcartesiano):
    
    def __init__(self,x,y,z,r=0,t=0,p=0): 
        vectorcartesiano.__init__(self,x,y,z)
        self.r=r
        self.t=t
        self.p=p
        
        if r<0:
            print("la coordenada r esta fuera del rango, introducir valores entre 0 <= r >= inf")
        if np.pi < t or t<0:
            print("la coordenada theta esta fuera del rango, introducir valores entre 0 <= theta >= pi")
        if 2 * np.pi < p  or p <0 :
            print("la coordenada phi esta fuera del rango, introducir valores entre 0 <= phi >= 2 pi")
            
        mp=np.sqrt(self.r**2+self.t**2+self.p**2)
        print("magnitud del vector polar:",mp)
        
    def prodpunto(self, other):
        print((self.r*other.r)+(self.t*other.t)+(self.p*other.p))
    
    def __add__(self,other):
        return vectorpolar(self.x, self.y, self.z, self.r+other.r, self.t+other.t, self.p+other.p)
           
    def __sub__(self,other):        
        return vectorpolar(self.x, self.y, self.z, self.r-other.r, self.t-other.t, self.p-other.p)
    
    def __eq__(self, other):    
        return vectorpolar(self.x, self.y, self.z ,self.r==other.r, self.t==other.t, self.p==other.p)
    
    def __getitem__(self,item):
        fp=[]
        fp.append(self.r)
        fp.append(self.t)
        fp.append(self.p)
        return fp[item-1] #tener en cuenta que la lista solo estaria tomando las 3 posiciones del vector polar
    
    def print(self):
        fe=[]
        fe.append(self.r)
        fe.append(self.t)
        fe.append(self.p)
        print(fe)
    
class trancartesianas(vectorpolar):
    
    def __init__(self,x,y,z,r,t,p):
        vectorpolar.__init__(self,x,y,z,r,t,p)
        
    def tran(self):
        return trancartesianas(self.r*np.sin(self.t)*np.cos(self.p),self.r*np.sin(self.t)*np.sin(self.p),self.r*np.cos(self.t),0,0,0)
    
    def print(self):
        fc=[]
        fc.append(self.x)
        fc.append(self.y)
        fc.append(self.z)
        print(fc)

        

