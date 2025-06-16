import sound
import time
import datetime
from pydub import AudioSegment


"""
Beeper производит звук точки или тире при нажатии кнопок мыши
	   Записывает сигналы и формирует аудиосегмент
	   Сохраняет аудиосегмент в файл
""" 
class Beeper:
	def __init__(self, frequency = 440, duration = 50):
		# точка
		self.dot_sound = sound.Sine_Sound(frequency = frequency,
											duration = duration)
		# тире
		self.dash_sound = sound.Sine_Sound(frequency = frequency,
											duration = duration * 3)
		# пробел			
		self.silence = sound.Sine_Sound(frequency = 0, duration  = duration)
		# флаг записи
		self.is_record_on = False
		
	def handle_signal(self, signal):
		t = time.time()
		sound = None
		if signal =='_':
			sound = self.dash_sound
		elif signal == '.':	
			sound = self.dot_sound			
						
		else:
			sound = self.silence
		
		sound.play()	
		
		
		# Если запись включена, то добавить в список сигналов
		# кортеж (сигнал, момент_времени)
		if self.is_record_on:
			self.signals.append((signal, t) )
			print(signal)
	
	def start_record(self): 
		self.signals = []
		if not self.is_record_on:
			start_time = time.time()
			# Начало 
			self.signals.append(('S', start_time))
			self.is_record_on = True
		
	def stop_record(self):
		if self.is_record_on:
			stop_time = time.time()
			# Конец
			self.signals.append(('F', stop_time))
			self.is_record_on = False
			
			# Вывод списка сигналов
			for signal in self.signals:
				print(signal[0], ' ', signal[1])
				
				
	"""
		Собирает аудиосегмент сегментов точки, тире и тишины.
		Пока не нажаты кнопки точки или тире, в общий аудиосегмент 
		добавляется аудиосегмент тишины
		Сохраняет в файл
	"""	
	def record_to_audio(self):
		self.audio = AudioSegment.empty()
		
		# промежуток времени между сигналами
		mid_time = 0.0
		i = 0 # счётчик
		for i in range(len(self.signals) - 1):
			# промежуток времени в секундах
			mid_time = self.signals[i+1][1] - self.signals[i][1] 
			
			# перевести длительность сигнала в секунды
			if self.signals[i][0] == '_':
				self.audio += self.dash_sound.sound
				mid_time = mid_time - self.dash_sound.duration / 1000
				
			elif self.signals[i][0] == '.':
				self.audio += self.dot_sound.sound
				mid_time = mid_time - self.dot_sound.duration / 1000
			
			else: 
				self.audio += self.silence.sound
				mid_time = mid_time - self.silence.duration / 1000				
			# Сделать тишину между сигналами                  
#			# перевести длительность промежутка в миллисекунды			
			self.audio += AudioSegment.silent(mid_time * 1000)
	
			print('signal ', self.signals[i][0])
			print('next signal ', self.signals[i+1][0], ' /','mt', mid_time)
		
		
		"""
		    Собирает аудиосегмент из точек и тире
		   
		"""
	def text_to_audio(self):
		self.audio = AudioSegment.empty()		
		i = 0 # счётчик
		for i in range(len(self.signals)):
			if self.signals[i][0] == '_':
				self.audio += self.dash_sound.sound
										
			elif self.signals[i][0] == '.':
				self.audio += self.dot_sound.sound
		
			# Тишина между точками и тире                  
			else:
				self.audio += self.silence.sound
		
		
		"""
		
		"""
	def text_to_morse(self, text):
		message_code = ''
		for i in range(len(text) ):
			message_code += morse_code.abc_code[text[i]]
			self.start_record()
	
		for l in message_code:
			self.handle_signal(l)
		
		#print("stop record")
		self.stop_record()
		#input("press to contuinue")
		self.text_to_audio()
		


	""" 
		Сохраняет в файл
	"""
	def save(self, file_name = 'morse_code', extens = 'mp3'):
		# cохраняем в файл
		fh = self.audio.export('{0}.{1}'.format(file_name, extens), format = 'mp3')
		
		
		

		
'''################################################################'''
		
import morse_code

if __name__ == '__main__':
	beeper = Beeper(duration = 80)
	
	message = 'I LOVE YOU'
	# переводит буквы в код 
	message_code = ''
	for i in range(len(message) ):
		message_code += morse_code.abc_code[message[i]]
	
	#message_code = '. . .   _ _ _   . . .'	
	
	print('CODE:', message_code)
	input("press to contuinue")
	
	print('start record')
	beeper.start_record()
	
	for l in message_code:
		beeper.handle_signal(l)
		
	print("stop record")
	beeper.stop_record()
	input("press to contuinue")
	beeper.text_to_audio()
	print('record has been made')
	# save to file
	beeper.save('beeper')



	
	
	
	
	
	
	
	
	
	'''
	должно определять слова кода в сообщении и выводить посимвольно
	
	input()
	sos = '... ___ ...     ...   ___   ...     ...   ___   ...'
	print("")
	sym_mes = ''	
	for i in range(len(sos) ):
		sym_mes += morse_code.code_abc[sos[i]]
	print(sym_mes)
	'''
#	beep.pause(3)


