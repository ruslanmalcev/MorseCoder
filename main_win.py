#! /usr/bin/python3

import tkinter as tk
import text_sound_win as ts
import telegraph_win as tlg

'''

программа должна открывать файл, проигрывать файл, преобразовывать музыкальный файл в 
график, выводить график, выводить знаки кода Морзе
Далее, возможно реализовать ввод кода Морзе с мыши, 
запись в файл звукового формата и т.д.


'''
class Main_Window(tk.Frame):
	def __init__(self, parent = None, **options):
		tk.Frame.__init__(self, parent, **options)
		self.pack()
		self.button_bar = tk.Frame(self)
		self.button_bar.pack(side = tk.TOP)
		self.tlg_button = tk.Button(self.button_bar, 
									text = 'Телеграф',
									command = self.show_telegraph)
		self.tlg_button.pack(side = tk.LEFT)
		
		self.text_sound_button = tk.Button(self.button_bar,
								text = 'Распознать звук',
								command = self.sound_transform)
		self.text_sound_button.pack(side =tk.LEFT)
		
		self.main_frame = tk.Frame(self)
		self.main_frame.pack(side = tk.TOP)
		self.main_widget = None
		self.show_telegraph()
		
	def show_telegraph(self):	
		if self.main_widget:
			self.main_widget.destroy()	
		
		self.main_widget = tlg.Telegraph_Window(self.main_frame)
			
	def sound_transform(self):		
		if self.main_widget:
			self.main_widget.destroy()

		self.main_widget = ts.Text_Sound_Window(self.main_frame)
			
			
if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x600')
	Main_Window(root)
	root.mainloop()


