from operator import mul
import numpy as np
from numpy.fft import rfft,irfft,fftfreq
from movie.editor import AudioFileClip
from movie.audio.AudioClip import AudioArrayClip
import matplotlib.pyplot as plt

fn = r'/home/pi/Desktop/jigong.mp3'
audio = AudioFileClip(fn)
t = np.arange(0, audio.duration, 1/audio.fps)
w = fftfreq(t.size, d=t[1]-t[0])
frames = audio.to_soundarray()
frames_fft = rfft(frames)
plt.plot(w, frames_fft, color='r')
frames_fft = frames_fft * 0.3
frames_fft = np.array(tuple(map(mul, frames_fft, np.sin(t))))
plt.plot(w, frames_fft, color='b')
frames_ifft = irfft(frames_fft).real
AudioArrayClip(frames_ifft,fps=audio.fps).write_audiofile('music.mp3')
plt.show()
