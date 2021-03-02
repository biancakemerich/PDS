# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:14:17 2021

@author: Bianca
"""
import numpy as np # arrays
import matplotlib.pyplot as plt # plots
plt.rcParams.update({'font.size': 10})
import sounddevice as sd
import soundfile as sf

#%% Importando os arquivos .wav
xt, fs = sf.read(r'C:\Users\Bianca\Documents\MeusProjetos\PDS\viola.wav')
time_xt = np.linspace(0, (len(xt)-1)/fs, len(xt))
ht, fs = sf.read(r'C:\Users\Bianca\Documents\MeusProjetos\PDS\ht.wav')
time_ht = np.linspace(0, (len(ht)-1)/fs, len(ht))

#%% Convolução dos sinais pela Propriedade

# calculo do tamnho do sinal resultante
n_x = len(xt)
n_h = len(ht[:,0])
N = n_x + n_h - 1

# TF do sinal anecoico (usar o argumento n_y faz com que xt seja completado com zeros no final)
Xjw = np.fft.fft(xt, N)

# TF das respostas ao impulso
HLjw = np.fft.fft(ht[:,0], N)
HRjw = np.fft.fft(ht[:,1], N)

# TF dos sinais de saída, convolução
YLjw = HLjw * Xjw
YRjw = HRjw * Xjw

# Transformadas de Fourier inversa
yt_l = np.fft.ifft(YLjw) # Canal esquerdo

yt_r = np.fft.ifft(YRjw) # Canal direito

time_yt = np.linspace(0, (len(yt_r)-1)/fs, len(yt_l))

#%% Plote dos sinais convoluidos no tempo
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.title(r'$y(t)$')
plt.plot(time_yt, np.real(yt_l), '-b', linewidth = 1, label = r'$y_L(t)$')
plt.legend(loc = 'upper right')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.xlim((0, time_yt[-1]))

plt.subplot(2,1,2)
plt.title(r'$y(t)$')
plt.plot(time_yt, np.real(yt_r), '-m', linewidth = 1, label = r'$y_R(t)$')
plt.legend(loc = 'upper right')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.xlim((0, time_yt[-1]))
plt.tight_layout()
plt.show()

#%% Reprodução de audio dos sinais da viola anecoico, e os convoluidos
yt_T = np.transpose([yt_l, yt_r]) # rearranjando os sinais em um vetor
sd.default.channels = 2 
#sd.play(xt, fs) # sinal da viola anecoico 
sd.play(np.real(yt_T), fs) # sinais convoluidos
