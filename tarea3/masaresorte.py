import numpy as np 

class oscilador: #resorte MAS
    
    def __init__(self,m=0,k=0,y0=0,t=0):
        self.m=m
        self.k=k
        self.y0=y0
        self.t=t
        
    def pos(self):
        p=[]
        for i in np.arange(0,self.t,0.1):
            p.append(self.y0*np.cos(np.sqrt(self.k/self.m)*i))
        return p
    
    def vel(self):
        vel=[]
        for i in np.arange(0,self.t,0.1):
            vel.append(-self.y0*np.sqrt(self.k/self.m)*np.sin(np.sqrt(self.k/self.m)*i))
        return vel        
        
    def time(self):
        ti=[]
        for i in np.arange(0,self.t,0.1):
            ti.append(i)
        return ti
    
    
    
    
class osciladorforzado(oscilador): #resorte subamortiguado
    
    def __init__(self,m=0,k=0,y0=0,t=0,gamma=0):
        oscilador.__init__(self,m,k,y0,t)
        self.gamma=gamma
        
    def posf(self):
        p=[]
        wp=np.sqrt((self.k/self.m)**2-(self.gamma/2)**2)
        for i in np.arange(0,self.t,0.1):
            p.append(self.y0*np.exp((-self.gamma*i)/2)*np.cos(wp*i))
        return p
    
    def velf(self):
        vel=[]
        wp=np.sqrt((self.k/self.m)**2-(self.gamma/2)**2)
        for i in np.arange(0,self.t,0.1):
            vel.append(-self.y0*wp*np.exp((-self.gamma*i)/2)*np.sin(wp*i)-self.y0*(self.gamma/2)*np.exp((-self.gamma*i)/2)*np.cos(wp*i))
        return vel        
        
    def timef(self):
        ti=[]
        for i in np.arange(0,self.t,0.1):
            ti.append(i)
        return ti
