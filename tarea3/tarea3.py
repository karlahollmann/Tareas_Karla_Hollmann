from masaresorte import oscilador, osciladorforzado
import matplotlib.pyplot as plt


#Oscilador armonico simple

mr1=oscilador(1,2,-3,10)
mr2=oscilador(1,2,5,10)
mr3=oscilador(1,2,-0.4,10)
#masa y constante de resorte diferente
mr4=oscilador(5,1,-3,10)
mr5=oscilador(5,1,5,10)
mr6=oscilador(5,1,-0.4,10)


#posicion vs tiempo

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.plot(mr1.time(),mr1.pos(),label="y0=-3m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(232)
plt.plot(mr2.time(),mr2.pos(), label="y0=5m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(233)
plt.plot(mr3.time(),mr3.pos(), label="y0=-0.4m, t=10s", color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(234)
plt.plot(mr4.time(),mr4.pos(), label="y0=-3m, t=10s")
plt.legend(fontsize=13)
plt.title('Posición vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(235)
plt.plot(mr5.time(),mr5.pos(), label="y0=5m, t=10s")
plt.legend(fontsize=13)
plt.title('Posición vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(236)
plt.plot(mr6.time(),mr6.pos(), label="y0=-0.4m, t=10s")
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.tight_layout()
plt.show()

#Velocidad vs tiempo

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.plot(mr1.time(),mr1.vel(),label="y0=-3m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(232)
plt.plot(mr2.time(),mr2.vel(), label="y0=5m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(233)
plt.plot(mr3.time(),mr3.vel(), label="y0=-0.4m, t=10s", color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(234)
plt.plot(mr4.time(),mr4.vel(), label="y0=-3m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(235)
plt.plot(mr5.time(),mr5.vel(), label="y0=5m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(236)
plt.plot(mr6.time(),mr6.vel(), label="y0=-0.4m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.tight_layout()
plt.show()

#oscilador forzaado subamortigado

mrf1=osciladorforzado(1,2,-3,10,3)
mrf2=osciladorforzado(1,2,5,10,3)
mrf3=osciladorforzado(1,2,-0.4,10,3)
#gamma pequeño
mrf4=osciladorforzado(5,1,-3,20,0.1)
mrf5=osciladorforzado(5,1,5,20,0.1)
mrf6=osciladorforzado(5,1,-0.4,20,0.1)

#posicion vs tiempo

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.plot(mrf1.timef(),mrf1.posf(),label="y0=-3m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(232)
plt.plot(mrf2.timef(),mrf2.posf(), label="y0=5m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(233)
plt.plot(mrf3.timef(),mrf3.posf(), label="y0=-0.4m, t=10s", color='green')
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(234)
plt.plot(mrf4.timef(),mrf4.posf(), label="y0=-3m, t=10s")
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(235)
plt.plot(mrf5.timef(),mrf5.posf(), label="y0=5m, t=10s")
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(236)
plt.plot(mrf6.timef(),mrf6.posf(), label="y0=-0.4m, t=10s")
plt.legend(fontsize=13)
plt.title('Posicion vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Posicion y (m)')
plt.xlabel('Tiempo (s)')
plt.grid()


plt.tight_layout()
plt.show()


#velocidad vs tiempo

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.plot(mrf1.timef(),mrf1.velf(),label="y0=-3m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(232)
plt.plot(mrf2.timef(),mrf2.velf(), label="y0=5m, t=10s",color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(233)
plt.plot(mrf3.timef(),mrf3.velf(), label="y0=-0.4m, t=10s", color='green')
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=1kg, k=2N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(234)
plt.plot(mrf4.timef(),mrf4.velf(), label="y0=-3m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidadvs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(235)
plt.plot(mrf5.timef(),mrf5.velf(), label="y0=5m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.subplot(236)
plt.plot(mrf6.timef(),mrf6.velf(), label="y0=-0.4m, t=10s")
plt.legend(fontsize=13)
plt.title('Velocidad vs Tiempo, m=5kg, k=1N/m')
plt.ylabel('Velocidad (m/s²)')
plt.xlabel('Tiempo (s)')
plt.grid()

plt.tight_layout()
plt.show()
