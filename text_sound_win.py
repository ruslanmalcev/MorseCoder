import tkinter as tk
import scrol_text
import graph_win
import player
from tkinter import filedialog
from pydub import AudioSegment
import translator

'''
Окно для вывода звукового файла в виде кода Морзе 
и текста
при нажатии кнопки "График"  в окне появляется график

'''
class Text_Sound_Window(tk.Frame):
	def __init__(self, parent = None, **options):
		tk.Frame.__init__(self, parent, **options)
		self.pack()
		
		self.button_bar = tk.Frame(self)
		self.button_bar.pack(side = tk.BOTTOM)

		self.main_widget = tk.Frame(self)
		self.main_widget.pack(side = tk.LEFT)
		
		self.morse_window = scrol_text.Scroll_Text(self.main_widget)
		self.morse_window.pack(side= tk.TOP, expand = tk.YES, fill = tk.BOTH)
		
		self.text_window = scrol_text.Scroll_Text(self.main_widget)	
		self.text_window.pack(side= tk.TOP, expand = tk.YES, fill = tk.BOTH)
		
		self.graph_frame = tk.Frame(self)
		self.graph_frame.pack(side = tk.RIGHT) 
				
		self.open_button = tk.Button(self.button_bar, text ='Открыть',
									command = self.open_file)
		self.open_button.pack(side = tk.LEFT)
		
		self.close_file_button = tk.Button(self.button_bar, text = 'Закрыть',
							command = self.close_file)
		self.close_file_button.pack(side = tk.LEFT)

		self.show_graph_button = tk.Button(self.button_bar, text= 'График',
							command = self.show_graph)
		self.show_graph_button.pack(side = tk.LEFT)

		self.play_sound_button = tk.Button(self.button_bar, text = 'Прослушать',
											command = self.play_sound)
		self.play_sound_button.pack(side = tk.LEFT)
		
		self.file = None
		self.graph_win = None
		self.data = []
		self.show_graph()
		self.trans = translator.Translator()
		
	def open_file(self):
		file_path = filedialog.askopenfilename(
		initialdir = '.', 
		title='Отрыть файл',
		filetypes = [('Audio files','*.mp3' or '*.wav'),('All files','*.*')]
		)
		if file_path:
			with open(file_path, 'r') as self.file:
				self.audio = AudioSegment.from_mp3(file_path)
		else: 
			return
		# перевести аудио в код Морзе
		self.data = self.trans.sound_to_code(self.audio)		
		
		# вывести код Морзе в окно
		with open('cache.txt', 'r') as file:
			text = file.read()
			
			#print(text)			
			num = []
			a = 0
			for i in range(1,len(text)):
				if text[i] == ' ':
					a+=1
				else:
					num.append(a)
					a = 0

			m = min(num)
			
			s = ''
			for i in range(len(text)):
				if text[i]!=' ':
					s+=text[i]
				elif text[i] == ' ':
					a+=1
					if text[i+1] != ' ':
						s += ' '*round(a/m)
						a = 0
			text = s
			
			self.morse_window.set_text(text)
			
		# перевести код Морзе в буквы
		trans_message = self.trans.code_to_text(text)
		self.text_window.set_text(trans_message)
		
	def close_file(self):
		if not self.file:
			return
		self.file.close()
		self.audio = AudioSegment.silent(10)
		self.morse_window.set_text()
		self.text_window.set_text()
		self.data = []
		self.show_graph()
		
	def show_graph(self):
		if self.graph_win: 
			self.graph_win.destroy()
		self.graph_win = graph_win.Graph_Window(self.graph_frame)
		self.graph_win.pack(side = tk.RIGHT)

		self.graph_win.set_data(self.data)
		self.graph_win.plot()
		
		
	

	def play_sound(self):
		player.Player().play_audio(self.audio)

if __name__ == '__main__':
	root = tk.Tk()
	mw = Text_Sound_Window(root)
	
	root.mainloop()
	
		
		
		
