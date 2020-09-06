#funcion factorial n!=1x2x3x...x(n-1)xn
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n):
            #se multiplica n por un i que varia de 1 hasta n-1
            n=n*i
        return n

#funcion binomial n!/(k!(n-k)!)
def binomial(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))


#Triangulo de pascal
def pascal(n):
    t=[]
    for m in range(0,n+1): #esta lista variara los valores de n de 0 a n
        fun=[]
        for k in range(0,n+1): #esta lista variara los valores de k de 0 a n
            l=binomial(m,k)
            if l>0: #elimina los valores de mas que deja los ciclos 
                fun.append(int(l)) #agregan los valores a una lista
        t.append(fun) #agrega los valores de cada n a una lista
        print("n=",m,"", fun)
    return "triangulo de pascal",t


