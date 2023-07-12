from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import windows
import pandas as pd


signal = pd.read_csv('spectrums/source_out_10k_1p.csv')
signal = signal.rename(columns={f'{signal.columns.values[0]}':'time',
                                f'{signal.columns.values[1]}':'Voltage'})

#Create transfer function LPF
f = np.linspace(1, 100e6, 500)
R=10e3
C=1e-12
HF = np.abs(1/(1+1j*R*C*2*np.pi*f))


#initial data for spectrums
N = len(signal.time)
dT = 1e-9
SAMPLE_RATE = 1/dT


#simple fft
yf = fft(signal.Voltage.values[0:N])
xf = fftfreq(N, 1/SAMPLE_RATE)

#apply window
#window list [blackman/boxcar/blackmanharris/hamming/hanning]
window = windows.boxcar(N)
ywf = fft(signal.Voltage.values[0:N]*window)

sig = np.abs(yf)
sig_w = np.abs(ywf)

plt.figure()
plt.plot(signal.time.values[0:N], signal.Voltage.values[0:N])

plt.figure()
plt.plot(xf[0:N//2], 20*np.log10((2/N)*sig[0:N//2]), label='fft')
plt.plot(xf[0:N//2], 20*np.log10((2/N)*sig_w[0:N//2]), label='fft+window')
plt.plot(f, 20*np.log10(HF)-50, label='TF')
plt.ylim((-70, 5))
plt.xlim((0, 50e6))
plt.legend()

plt.show()