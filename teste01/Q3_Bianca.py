# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:03:59 2020

Questão 3

@author: Bianca 
"""
# importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

def H(t):
    '''
    Definição da função degrau unitário 
    '''
    return np.where(t < 0, 0.0, 1.0)

def x(t):
   '''
   Função descontínua dada pela questão
   '''
   x = np.zeros(len(t)) #vetor de zeros criado com o tamanho de t para inserir os valores da função em cada valor de t
   x[t>=-2] = t+1 
   x[t>=-1] = 1
   x[t>=0] = 2
   x[t>=1] = [ 2-i for i in np.arange(1, 2, 0.01)] #loop criado para limitar os valores de x para até t<2
   return x

t = np.arange(start = -2, stop = 2, step=0.01) # vetor temporal

#chamando as funções
xt = x(t) 
u = H(t)

#fazendo a operação das funções pedida na questão
f = (xt + np.flip(xt))*u

#plotando o gráfico
plt.figure(figsize=(10,7))
plt.plot(t, f, '-b', label = r'$[x(t) + x(-t)]u(t)$')
plt.legend(loc = 'upper right')
plt.grid(linestyle = '--', which='both')
plt.xlabel('tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()   
plt.show()