# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:49:42 2021

@author: gabri

Me baseei muito nas aulas 54, 55 e em seus respectivos notebooks

"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm
from scipy import signal

# Frequencia de amostragem e vetor temporal
fs = 2000
time = np.arange(0, 2, 1/fs)

#definindo amplitudes
a = 7
b = 5
c = 2
t1 = 0.1
t2 = 0.4
#ruído branco
st = np.random.normal(loc = 0, scale = 1, size = len(time))

#ruídos entrada e saída
n_1 = np.random.normal(loc = 0, scale = 0.1, size = len(time))
n_2 = np.random.normal(loc = 0, scale = 0.5, size = len(time))

# sinal entrada
xt = a*st

#sinal saída
yt = np.zeros(len(time)) + st + n_1 

#sinal de saída com eslocamento 
yt = b*np.roll(st, int(-t1*fs)) + c*np.roll(st, int(-t2*fs))
#yt[int(t1*fs):] = yt[int(t1*fs):] + b * st[:len(time)-int(t1*fs)] 
#yt[int(t2*fs):] = yt[int(t2*fs):] + c * st[:len(time)-int(t2*fs)] 

#sinais com ruído
xt_n1 = xt + n_1
yt_n2 = yt + n_2

# plot signal
plt.figure(figsize = (10, 3))
plt.title('Sinal x(t) com ruído')
plt.plot(time, xt_n1, linewidth = 1)
plt.grid(linestyle = '--', which='both')
plt.ylabel(r'$x(t)$ [Pa]')
plt.xlim((0, time[-1]))
plt.ylim((-35, 35))
plt.xlabel('Tempo [s]')
plt.tight_layout()

plt.figure(figsize = (10, 3))
plt.title('Sinal y(t) com ruído')
plt.plot(time, yt_n2, linewidth = 1, color ="g")
plt.grid(linestyle = '--', which='both')
plt.ylabel(r'$y(t)$ [Pa]')
plt.xlim((0, time[-1]))
plt.ylim((-35, 35))
plt.xlabel('Tempo [s]')
plt.tight_layout()

#Auto correlação

Rxx = np.correlate(xt_n1, xt_n1, mode = 'same')
Ryy = np.correlate(yt_n2, yt_n2, mode = 'same')

#Correlação cruzada

Rxy = np.correlate(xt_n1, yt_n2, mode = 'same')

#Deslocamento no tempo (baseado na aula 55)
tau = np.linspace(-0.5*len(Rxy)/fs, 0.5*len(Rxy)/fs, len(Rxy))

#plots
# autocorrelação
plt.figure(figsize = (12, 5))
plt.title('Autocorrelação do sinal x(t)')
plt.plot(tau, Rxx/len(Rxx), linewidth = 1, color='b')
plt.grid(linestyle = '--', which='both')
plt.ylabel(r'$R_{xx}(\tau)$')
plt.xlabel(r'$\tau$ [s]')
plt.tight_layout()

plt.figure(figsize = (12, 5))
plt.title('Autocorrelação do sinal y(t)')
plt.plot(tau, Ryy/len(Ryy), linewidth = 1, color='g')
plt.grid(linestyle = '--', which='both')
plt.ylabel(r'$R_{yy}(\tau)$')
plt.xlabel(r'$\tau$ [s]')
plt.tight_layout()

# Correlação cruzada
plt.figure(figsize = (12, 5))
plt.title('Correlaçãocruzada dos sinais x(t) e y(t)')
plt.plot(tau,Rxy/len(Rxy), linewidth = 1, color='b')
plt.grid(linestyle = '--', which='both')
plt.ylabel(r'$R_{xy}(\tau)$')
plt.xlabel(r'$\tau$ [s]')
plt.tight_layout()

