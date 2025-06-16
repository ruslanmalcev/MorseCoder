from pydub.generators import Sine
from pydub.playback import play

class Sine_Sound:
	def __init__(self, sample_rate = 44100, frequency = 440, duration = 1000):
		self.sample_rate = sample_rate
		self.tone = Sine(frequency, sample_rate = sample_rate)
		self.frequency = frequency
		self.duration = duration
		self.sound= self.tone.to_audio_segment(duration)
	
	def play(self):
		play(self.sound)






if __name__ == '__main__':
	sine = Sine_Sound(frequency = 880, duration = 100)
	silent = Sine_Sound(frequency = 0, duration = 900)
	sine_fin = Sine_Sound(frequency = 880, duration = 1000)
	
	for i in range(4):
		sine.play()
		silent.play()
	sine_fin.play()
	
	# далее играет музыка Свиридова "Время вперёд"
	
