# -*- coding: utf-8 -*-
"""
UW GIX
Techin 512
Lab 7
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('zia-ex.txt')

def exponential_decay_filter(signal, alpha):

    signal_filtered = np.zeros(len(signal))
    signal_filtered[0] = signal[0]
    for i in range(1, len(signal)):
        signal_filtered[i] = alpha*signal[i] + (1-alpha)*signal_filtered[i-1]
    return signal_filtered

time = data[:,0]
ppg_reading = data[:,1]

ppg_reading_filtered_1 = exponential_decay_filter(signal = ppg_reading, alpha = 0.5)
ppg_reading_filtered_2 = exponential_decay_filter(signal = ppg_reading, alpha = 0.2)
ppg_reading_filtered_3 = exponential_decay_filter(signal = ppg_reading, alpha = 0.1)

ax = plt.figure(figsize=(18,8))

plt.plot(time, ppg_reading, label = 'raw')
plt.plot(time, ppg_reading_filtered_1, label = r'$\alpha =0.5$')
plt.plot(time, ppg_reading_filtered_2, label = r'$\alpha =0.2$')
plt.plot(time, ppg_reading_filtered_3, label = r'$\alpha =0.1$')

plt.grid()
plt.locator_params(nbins=40, axis='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Sensor Reading')
plt.title('PPG - Exponential decay filter')
plt.legend()
plt.show()
