# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:03:59 2020

Questão 5
Código desenvolvido para calcular o valor médio e RMS de sinais periódicos

@author: Bianca 
"""
# importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

Tp = 1 #período
f = 1 #frequência
t = np.linspace(0, Tp, 1000) #vetor temporal
A = 12 #amplitude
w = 2*np.pi*f #omega
xt = A*np.sin(w*t) #equação do sinal

x0 = np.mean(xt) #valor médio do sinal
xrms = np.sqrt(np.mean(xt**2)) #valor rms do sinal

print(f'Valor Médio: {x0:.3f}')
print(f'Valor RMS: {xrms:.3f}')

#plotando o gráfico
plt.figure()
plt.title('Sinal do Valor médio e RMS (i)')
plt.plot(t, xt, 'b', label = r'$x(t)$')
plt.plot(t,x0*np.ones(len(t)),'--k', label = r'$x_0$')
plt.plot(t,xrms*np.ones(len(t)),'--r', label = r'$x_{rms}$')
plt.legend(loc = 'upper right')
plt.grid(linestyle = '--', which='both')
plt.xlabel('tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()   
plt.show()

#%% (ii)

Tp = 1 #período
f = 1 #frequência
t = np.linspace(0, Tp, 1000) #vetor temporal
A = 8 #amplitude do sinal
A0 = 3 #deslocamento do sinal
w = 2*np.pi*f #omega
xt = A0 + A*np.sin(w*t) #equação do sinal

x0 = np.mean(xt) #valor médio do sinal
xrms = np.sqrt(np.mean(xt**2)) #valor rms do sinal

print(f'Valor Médio: {x0:.3f}')
print(f'Valor RMS: {xrms:.3f}')

#plotando o gráfico
plt.figure()
plt.title('Sinal do Valor médio e RMS (ii)')
plt.plot(t, xt, 'b', label = r'$x(t)$')
plt.plot(t,x0*np.ones(len(t)),'--k', label = r'$x_0$')
plt.plot(t,xrms*np.ones(len(t)),'--r', label = r'$x_{rms}$')
plt.legend(loc = 'upper right')
plt.grid(linestyle = '--', which='both')
plt.xlabel('tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()   
plt.show()
