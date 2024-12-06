import matplotlib.pyplot as plt
import numpy as np

power = 1024

x_axis = np.arange(0,10,10/power)
y_axis = np.random.random(power)/10
t = np.arange(power)
sinus = np.sin(t)
y_axis -= sinus

plt.subplot(2,1,1)
plt.plot(x_axis, y_axis)
plt.title('Simulated EEG Signal (Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

x_axis = np.arange(0,100,100/power)
fft = np.fft.fft(y_axis)

plt.subplot(2,1,2)
plt.plot(x_axis[1:], fft[1:])
plt.title('Frequency Spectrum of EEG signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.axvspan(8, 13, color = 'yellow', alpha = 0.3)
plt.axvspan(13, 30, color = 'green', alpha = 0.3)
plt.axvspan(30, 100, color = 'red', alpha = 0.3)
plt.legend(['Frequency Spectrum', 'Alpha', 'Beta', 'Gamma'])

plt.tight_layout()

plt.show()

