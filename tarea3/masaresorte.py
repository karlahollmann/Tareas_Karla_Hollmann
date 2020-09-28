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
    
   
    from scipy.integrate import odeint
    #resolver las ec con odeint
    #Movimiento armonico simple
    def ecmovMAS(y,t,k,m):
        y1=y[0]
        y2=y[1]
        dy1=y2 #se define y2 como la derivada de y1
        dy2=-(k/m)*y1
        return [dy1,dy2]
    
    #Se definen las condiciones iniciales y0=[y0x,y0v]
    #Se crea un intervalo de tiempo 
    #sol = odeint(ecmovMAS, y0, t, args=(k,m))
    #y=sol[:,0]
    #para graficar basta con hacer el plot con la posicion y el intervalo de tiempo
    
    #oscilador forzado
    def ecmovOF(y,t,k,m,gamma):
        y1=y[0]
        y2=y[1]
        dy1=y2 #se define y2 como la derivada de y1
        dy2=-gamma*y2-(k/m)*y1
        return [dy1,dy2]
    
    #condiciones iniciales y0=[y0x,y0v]
    #sol = odeint(ecmovOF, y0, t, args=(k,m,gamma))
    
