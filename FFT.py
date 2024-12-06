import numpy as np

def fft(lst):
    """
    Fast Fourier Transform
    :param lst: The input list
    :return: The FFT result
    :raises: ValueError if the length of the input list is not a power of 2
    """
    length = len(lst)
    if length & (length - 1):
        raise ValueError("The length of the input list must be a power of 2")
    if length <= 1:
        return lst
    w = np.exp(-2j * np.pi / length)
    even = fft(lst[0::2])
    odd = fft(lst[1::2])
    y = [even[j] + w**j * odd[j] for j in range(length // 2)]
    y += [even[j] - w**j * odd[j] for j in range(length // 2)]
    return y