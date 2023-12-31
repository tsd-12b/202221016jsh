# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h2a2hsAwwHc7h4qn-AgtZYjHkSYfQXfV
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control

st.title('Graphs')

#전달 함수 정의
G = control.TransferFunction([100],[1,5,6])

# 폐루프 전달함수 계산
G1 = control.feedback(G)

st.subheader("Transfer Function G(s):")
st.write(G1)

#단위 계산 응답
num = [100]
den = [1,5,106]

system = signal.TransferFunction(num, den)

#단위 계단 응답
t, y = signal.step(system)

#그래프 그리기: 단위 계단 응답
fig, ax = plt.subplots()
ax.plot(t, y)
ax.set(xlabel='Time(s)', ylabel='Response', title='Step Response of H(s) = 100 / (s + 2) * (s + 3)')
ax.grid()

#그래프 표시
st.pyplot(fig)

G0 = signal.lti([100],[1])
G1 = signal.lti([1],[1,2])
G2 = signal.lti([1],[1,3])
G3 = signal.lti([100],[1,5,6])

frequencies = np.logspace(-2,2,500)

systems = [G0,G1,G2,G3]
labels = ['Proportional Element', 'Integral Element', 'First-Order Lag Element', 'Overall System']
colors = ['r', 'g', 'b', 'm']

fig, ax = plt.subplots(figsize=(12,8))

# Bode magnitude plot
ax1 = plt.subplot(2,1,1)
for sys,label,color in zip(systems, labels, colors):
  w, mag, _ = sys.bode(frequencies)
  plt.semilogx(w, mag, color=color, label=label)
plt.title('Bode plot')
plt.ylabel('Magnitude [dB]')
plt.legend()

# Bode phase plot
ax2 = plt.subplot(2,1,2)
for sys,_,color in zip(systems, labels, colors):
  w, _, phase = sys.bode(frequencies)
  plt.semilogx(w, phase, color=color)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')

#그래프 표시
st.pyplot(fig)
