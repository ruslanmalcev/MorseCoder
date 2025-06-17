import sound
from pydub import AudioSegment
from pydub.playback import play
'''
проигрывает запись и звуки 


'''
class Player:
	def __init__(self):
		
		self.silence = sound.Sine_Sound(frequency = 0, duration = 5)
		
		
	
	def play_audio(self, audio):
		assert isinstance(audio, AudioSegment), 'Неправильный файл'
		print("start play")
		play(audio)
		print("stop play")
			
		
		
	

		
	

	
