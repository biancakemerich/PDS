# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 07:00:53 2021

@author: Bianca
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import signal

fs =  1000 # frequência de amostragem
t = np.arange(0, 2, 1/fs)

# constantes dos sinais
a = 1
b = 0.8
c = 0.75
delta1 = 0.25
delta2 = 0.5

# sinal emitido x(t) com s(t) -> ruído branco
st = np.random.normal(loc = 0, scale = 1, size = len(t))
nx = np.random.normal(loc = 0, scale = 0.1, size = len(t)) # ruído gaussiano
xt = a*st + nx

# sinal no receptor y(t) = y1 + y2
ny = np.random.normal(loc = 0, scale = 0.5, size = len(t)) # ruído gaussiano
yt = np.zeros(len(t)) + st + ny
yt = b*np.roll(st, int(-delta1*fs)) + c*np.roll(st, int(-delta2*fs))

#%% plot dos sinais x(t) e y(t)

plt.figure(figsize = (10, 6))
plt.subplot(2,1,1)
plt.plot(t, xt, linewidth = 1, color='b', alpha = 0.7)
plt.grid(linestyle = '--', which='both')
plt.title('Sinal emitido e contaminado por ruído')
plt.ylabel(r'$x(t)$')
plt.xlabel('Tempo [s]')
plt.xlim((0, t[-1]))
plt.ylim((-5, 5))

plt.subplot(2,1,2)
plt.plot(t, yt, linewidth = 1, color='m', alpha = 0.7)
plt.grid(linestyle = '--', which='both')
plt.title('Sinal gravado e contaminado por ruído')
plt.ylabel(r'$y(t)$')
plt.xlabel('Tempo [s]')
plt.xlim((0, t[-1]))
plt.ylim((-5, 5))
plt.tight_layout()

#%% Calculo das auto-correlações e correlações cruzadas

#Auto correlação de x(t)
Rxx = np.correlate(xt, xt, mode = 'same')
Ryy = np.correlate(yt, yt, mode = 'same')

#Correlação cruzada
Rxy = np.correlate(xt, yt, mode = 'same')
tau = np.linspace(-0.5*len(Rxy)/fs, 0.5*len(Rxy)/fs, len(Rxy))

#%% Plot das auto-correlações de x(t) e y(t)

plt.figure(figsize = (10, 6))
plt.subplot(2,1,1)
plt.plot(tau, Rxx/len(Rxx), linewidth = 1, color='b', alpha = 0.7)
plt.grid(linestyle = '--', which='both')
plt.title('Auto-correlação do sinal $x(t)$')
plt.ylabel(r'$R_{xx}(\tau)$')
plt.xlabel(r'$\tau$ [s]')

plt.subplot(2,1,2)
plt.plot(tau, Ryy/len(Ryy), linewidth = 1, color='m', alpha = 0.7)
plt.grid(linestyle = '--', which='both')
plt.title('Auto-correlação do sinal $y(t)$')
plt.ylabel(r'$R_{yy}(\tau)$')
plt.xlabel(r'$\tau$ [s]')

plt.tight_layout()

#%% Plot da correlação cruzada Rxy(tau)

plt.figure(figsize = (10, 3))
plt.plot(tau, Rxy/len(Ryy), linewidth = 1, color='g')
plt.grid(linestyle = '--', which='both')
plt.title(r'Correlação cruzada de $x(t)$ e $y(t)$')
plt.ylabel(r'$R_{xy}(\tau)$')
plt.xlabel(r'$\tau$ [s]')
plt.tight_layout()



























