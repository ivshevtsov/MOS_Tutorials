from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import windows
import pandas as pd



signal = pd.read_csv('spectrums/source_out.csv')
signal = signal.rename(columns={'out_source X':'time', 'out_source Y':'Voltage'})

N = len(signal.time)
dT = 1e-9
SAMPLE_RATE = 1/dT
print(signal.Voltage.values)

# число точек в normalized_tone
#N = SAMPLE_RATE * DURATION

yf = fft(signal.Voltage.values)
window = windows.boxcar(N)
ywf = fft(signal.Voltage.values*window)
xf = fftfreq(N, 1/SAMPLE_RATE)

sig = np.abs(yf)
sig_w = np.abs(ywf)

plt.plot(xf[0:N//2], 20*np.log10((2/N)*sig[0:N//2]))
plt.plot(xf[0:N//2], 20*np.log10((2/N)*sig_w[0:N//2]))
plt.ylim((-70, 5))
plt.xlim((0, 50e6))
plt.show()