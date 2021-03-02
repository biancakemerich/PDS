# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:50:16 2021

@author: Bianca

Seja o sinal contínuo x(t) = exp(-10 t) u(t). 
Crie um programa em que a versão amostrada do sinal é criada 
com taxas de Fs = 100 Hz e Fs = 1000 Hz.
Compare os espectros analítico e calculados via FFT para as duas taxas de amostragem.
Tente escrever nos comentários ou em texto (no arquivo do programa) as 
razões para as diferenças,
maior ou menor precisão.
"""
# importando bbt
import numpy as np # arrays
import matplotlib.pyplot as plt # plots
plt.rcParams.update({'font.size': 12})

Fs1 = 100 #taxa de amostragem
t = np.arange(0, 1, 1/Fs1) #vetor período
xt = np.zeros(len(t)) #Criação de um vetor de zeros para a função do sinal de entradal
xt[t>=0] = np.exp(-10*t[t>=0]) #Sinal no dominio do tempo

Xw = np.fft.fft(xt) #TF sinal no dominio da frequência
N = len(xt) #número de amostras
freq = np.linspace(0, (N-1)*Fs1/Fs1, N)

plt.figure()
plt.title("Espectro Analítico")
plt.stem(t, xt, '-b', label = f"$F_s = {Fs1}$ [Hz]", basefmt=" ", use_line_collection=  True) #espectro analítco
plt.legend(loc = 'upper right')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')

plt.figure()
plt.title("Espectro Calculado pela FFT")
plt.plot(freq, np.abs(Xw)/N, 'b', linewidth = 2)
plt.axvline(Fs1/2, color='k',linestyle = '--', linewidth = 4, alpha = 0.8)
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [-]')
plt.grid(which='both', axis='both')
plt.xlim((0,Fs1))

#%% Taxa de amostragem = 1000 Hz
Fs1 = 1000
t = np.arange(0, 1, 1/Fs1)
xt = np.zeros(len(t)) #Criação de um vetor de zeros para a função do sinal de entradal
xt[t>=0] = np.exp(-10*t[t>=0]) #Sinal no dominio do tempo

Xw = np.fft.fft(xt) #TF sinal no dominio da frequência
N = len(xt) #número de amostras
freq = np.linspace(0, (N-1)*Fs1/Fs1, N)

plt.figure()
plt.title("Espectro Analítico")
plt.stem(t, xt, '-b', label = f"$F_s = {Fs1}$ [Hz]", basefmt=" ", use_line_collection=  True) #espectro analítco
plt.legend(loc = 'upper right')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')

plt.figure()
plt.title("Espectro Calculado pela FFT")
plt.plot(freq, np.abs(Xw)/N, 'b', linewidth = 2)
plt.axvline(Fs1/2, color='k',linestyle = '--', linewidth = 4, alpha = 0.8)
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [-]')
plt.grid(which='both', axis='both')
plt.xlim((0,Fs1))

