import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#, NavigationToolbar2Tk

class Graph_Window(tk.Frame):
	def __init__(self, parent = None, data = None, **options):
		tk.Frame.__init__(self, parent, **options)
		self.data = data
		self.plot_button = tk.Button(self, text = 'Plot',
							command = self.plot)
		#self.plot_button.pack(side = tk.BOTTOM)		
		
	def set_data(self, data):
		self.data = data
				
	def plot(self):		
		self.figure = Figure(figsize = (3, 4),
							dpi = 100)
		
		time_audio = [i for i in range(0,len(self.data))]

		p = self.figure.add_subplot(111)
		p.plot(time_audio, self.data)

		self.canvas = FigureCanvasTkAgg(self.figure,
										master = self )
		self.canvas.draw()
		self.canvas.get_tk_widget().pack()
		
	



if __name__ == '__main__':
	root = tk.Tk()
	Graph_Window(root)
	root.mainloop()
	
