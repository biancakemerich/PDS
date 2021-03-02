# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:06:32 2021

@author: Bianca
"""
# importar as bibliotecas necessárias
import numpy as np # arrays
import matplotlib.pyplot as plt # plots
plt.rcParams.update({'font.size': 10})
#import IPython.display as ipd # to play signals
from scipy import signal
import sounddevice as sd
import soundfile as sf

Fs = 50
t = np.arange(0, 0.5, 1/Fs) 
xt = 2*np.sin((2*np.pi*10*t) + (np.pi/2))
N = len(xt) 

# FFT
Xw = np.fft.fft(xt, N)
freq = np.linspace(0, (N-1)*Fs/N, N)

#%%
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(t, xt, '-b', linewidth = 1)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
#plt.xlim((0, 1))
#plt.ylim((-2, 2))

plt.subplot(1,2,2)
#plt.semilogx(freq, 20*np.log10(2*np.abs(Xw)/N), '-b', linewidth = 2)
plt.plot(freq, (2*np.abs(Xw))/N, '-b', linewidth = 2)
plt.axvline(Fs/2, color='grey',linestyle = '--', linewidth = 4, alpha = 0.4)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [-]')
plt.xlim((5, Fs))
plt.tight_layout()
plt.show()