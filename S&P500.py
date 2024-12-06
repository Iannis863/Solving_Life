import yfinance as yf
import matplotlib.pyplot as plt
from FFT import fft

sp500 = yf.Ticker("^GSPC")
hist = sp500.history(period="max")

plt.figure(figsize=(10, 6))
plt.subplot(2,1,1)
plt.plot(hist.index, hist['Close'], label='S&P 500')
plt.title('S&P 500 Index')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(range(16384), fft(hist['Close'][7962:]), label='S&P 500')
plt.title('Frequency Spectrum of S&P 500 Index (FFT)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()