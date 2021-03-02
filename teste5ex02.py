# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:56:05 2021

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

#%%  (1) - plote o sinal no tempo com a correta escala de tempo e amplitude
xg, fs = sf.read(r'cricket5.wav')
xt = xg[:,0]
time = np.linspace(0, (len(xt)-1)/fs, len(xt))
#sd.play(xt, fs) # sinal da viola anecoico 
Xw = np.fft.fft(xt)
N = len(xt)
freq = np.linspace(0, (N-1)*fs/N, N)

plt.figure()
plt.plot(time, xt, '-b', linewidth = 1)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.show()

#%% (2) - Calcule a FFT e plote a magnitude do espectro em dB com a correta escala de frequência e amplitude
plt.figure()
plt.plot(freq, 20*np.log10((2*np.abs(Xw))/N), '-b', linewidth = 0.5)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [dB]')
plt.xlim((0,fs/2))
plt.tight_layout()
plt.show()

#%%(3) - Escreva na tela uma mensagem dizendo qual é a resolução do espectro calculado no item 2. 
#A mensagem deve ser algo como "A resolução do espectro calculado com a FFT é X [Hz]"
print(f'A resolução do espectro calculado com a FFT é {freq[1]-freq[0]:.2f} [Hz]')

#%% (4) - Calcule e plote um espectrograma de magnitude do sinal
win = signal.windows.hann(4096)
f, t, Sxx = signal.spectrogram(xt, fs, window = win, noverlap = len(win)/2, scaling = 'spectrum')

plt.figure(figsize=(15,6))
p = plt.pcolormesh(t, f, 10*np.log10(Sxx/np.amax(Sxx)), shading='gouraud', cmap = 'RdBu',vmin = -80)
plt.colorbar(p)
plt.ylim((80, 17500))
#plt.yscale('log')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#%% Escreva na tela uma mensagem dizendo qual é a resolução em tempo e frequência do espectrograma no item 4
print(f'A resolução temporal do espectrograma é de {t[1]-t[0]:.2f} [s] e em frequência é de {f[1]-f[0]:.2f} [Hz]')
