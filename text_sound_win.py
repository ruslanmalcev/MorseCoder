import tkinter as tk
import scrol_text
import graph_win
import player
from pydub.playback import play
from tkinter import filedialog
from pydub import AudioSegment
import Morse

'''
Окно для вывода звукового файла в виде кода Морзе 
и текста
при нажатии кнопки "График" выводится отдельное окно с графиком

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
		self.graph_win = None
	
	def open_file(self):
		file_path = filedialog.askopenfilename(
		initialdir = '.', 
		title='Выбирете файл',
		filetypes = [('Audio files','*.mp3' or '*.wav'),('All files','*.*')]
		)
		if file_path:
			with open(file_path, 'r') as self.file:
				self.audio = AudioSegment.from_mp3(file_path)
		self.data = self.transform()
		
		
	def show_graph(self):
		if self.graph_win: 
			self.graph_win.destroy()
		self.graph_win = graph_win.Graph_Window(self.graph_frame)
		self.graph_win.pack(side = tk.RIGHT)

		self.graph_win.set_data(self.data)
		self.graph_win.plot()
		
		
	def close_file(self):
		self.file.close()
		self.audio = AudioSegment.silent(10)
		self.morse_window.set_text()
		self.text_window.set_text()
		self.graph_win.destroy()
		
	def transform(self):
		audio_array = self.audio.get_array_of_samples()
		audio_array_1 = Morse.abs_lst(audio_array)
		audio_array_2 = Morse.bin_list(audio_array_1)
			
		m = max(audio_array_1) # Максимальное значение
		sr = sum(audio_array_1)/len(audio_array_1) # Среднее значение
		sens =  sr/m # Чувствительность сигнала
		accur = 1 - (sens)**2
			
		lst_1 = Morse.first_del_zeros(audio_array_2, accur)
		lst_2 = Morse.trans_strlist_numlist(Morse.second_del_zeros(lst_1, accur/2))
			
		lis = Morse.seq_numbers(lst_2)
		#print(lis)
		lis_skelet = Morse.struct_list(lst_2)
		#print(lis_skelet)
		if lis_skelet[0] == 0:  #Удаляет нули в начале
			lis_skelet = lis_skelet[1:]
			lis = lis[1:]
		if lis_skelet[-1] == 0:  #Удаляет нули в конце
			lis_skelet = lis_skelet[:-1]
			lis = lis[:-1]

		#point = min(lis) #Point
		one_list = [lis[i] for i in range(len(lis)) if lis_skelet[i] == 1]
		#print(one_list)
		dash = max(one_list)
		point = dash//3
		ratio = point/max(one_list) # Отношение точки к максимальному элементу

		#print('Point length: ',point)
		#print(ratio)
		string = ''	# Переводим массив чисел в азбуку Морзе
		for i in range(len(lis)):
			if lis[i] <= point or lis_skelet[i]==0:
				n = round(lis[i]/point)
			elif lis[i] > point and lis_skelet[i] == 1:
				if point/lis[i]<=lis[i]/(3*point):
					n = 3
			else:
				n = 1
					
			if lis_skelet[i]==0:
				string+=' '*n
			elif lis_skelet[i]==1:
				if n > 1:
					string+='_'
				else:
					string += '.'
			
		my_file = open('cache.txt', 'w+')
		my_file.write(string)
		my_file.close()
			
		with open('cache.txt', 'r') as file:
			text = file.read()
			self.morse_window.set_text(text)
		
		return lst_2	

	def play_sound(self):
		play(self.audio)

if __name__ == '__main__':
	root = tk.Tk()
	mw = Text_Sound_Window(root)
	
	root.mainloop()
	
		
		
		
