import numpy as np

k=1.38e-23
T=300
B=500e3
NF=6
ADC_FS=4
Noise_level = 10*np.log10(k*T*B*1000)
#Noise_level=-108
LNA=19
MIX=19
LPF=16


IN_NOISE=Noise_level+NF
MAX_GAIN=ADC_FS-IN_NOISE
VGA_MAX=MAX_GAIN-LNA-MIX-LPF

print(f'Noise level {Noise_level} dbm')
print(f'Noise level+NF {IN_NOISE} dBm')
print(f'Required Gain {MAX_GAIN} dB')
print(f'VGA_MAX {VGA_MAX} dB')

print('Lower band from another config')

