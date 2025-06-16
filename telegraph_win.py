#! /usr/bin/python3
# telegraph_win.py

import tkinter as tk
from scrol_text import Scroll_Text
import player
import beeper
import tkinter.filedialog 

'''
Окно для ввода кода Морзе с помощью кнопок мыши
по принципу работы телеграфного ключа
Кнопка Запись начинает запись сообщения
Кнопка Стоп останавливает запись сообщения

'''
class Telegraph_Window(tk.Frame):	
	def __init__(self, parent = None, **options):
		tk.Frame.__init__(self, parent, **options)
		self.pack()
		self.is_record_on = False		
		'''Beeper проигрывает звуки и записи при 
		нажатии кнопок мыши, он производит звук точки или тире
		Записывает сигналы и формирует файл
		
		''' 
		self.beeper = beeper.Beeper(frequency = 600, duration = 100)
				
		self.message_text = Scroll_Text(self)
		self.message_text.pack()
		self.trans_button = tk.Button(self, text = 'Перевести',
								command = self.transform)
		self.trans_button.pack(side = tk.TOP)
		
		self.label = tk.Label(self, 
					text= 'Левая кнопка - точка\nПравая кнопка - тире')
		self.label.pack(anchor = tk.CENTER, expand = tk.YES, fill = tk.BOTH)
		self.label.config(height = 16, width = 40, bg = 'light green')
		
		self.make_bindings()
		
		self.record_button = tk.Button(self, text = 'Запись',
									command = self.start_record)
		self.record_button.pack(side = tk.LEFT)
		
		
		
		self.stop_record_button = tk.Button(self, text = 'Стоп',
									command = self.stop_record)
		self.stop_record_button.pack(side = tk.LEFT)
		
		
		self.message_bar = tk.Label(self, width = 40,
									height = 1,
									borderwidth = 2,
									relief = tk.SUNKEN)
		self.message_bar.pack(side =tk.LEFT)
		
		self.save_button = tk.Button(self, text = 'Сохранить',
									 command = self.save_to_file)
		self.save_button.pack(side = tk.RIGHT)
	
	'''#######################################################'''
	def make_bindings(self):
		self.label.bind('<Button-1>', (lambda event, sig = '.': 
							self.signal(event, sig) ) ) 
		self.label.bind('<Button-3>', (lambda event, sig = '_':
							self.signal(event, sig) ) ) 
		
	def signal(self, event, sig):
		self.beeper.handle_signal(sig)
		
	""" Начать запись"""	 
	def start_record(self):
		self.message_bar.config(text = 'Идёт запись...')
		self.beeper.start_record()
	
	""" Остановить запись"""
	def stop_record(self):
		self.beeper.stop_record()
		self.message_bar.config(text = 'Запись остановлена!')
		
	def save_to_file(self):
		'''
		окно для сохранения в файл
		'''
		file_path = tk.filedialog.asksaveasfilename(
			initialdir = '.', 
			title='Сохранить как',
			filetypes = [('Audio files','*.mp3'),('All files','*.*')]
			)
		if file_path:
			self.beeper.record_to_audio()
			self.beeper.save(file_path)
		else:
			print("Файл не выбран")
			
	""" Переводит текст в звук кода Морзе """	
	def transform(self):
		self.beeper.text_to_morse(self.message_text.get_text())
		
	'''########################################################'''		
	
	
	
	
	
if __name__ == '__main__':
	root = tk.Tk()
	root.title('Телеграф')
	#root.minsize('600x480')
	Telegraph_Window(root)
	root.mainloop()
