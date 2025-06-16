import tkinter as tk

class Scroll_Text(tk.Frame):
	def __init__(self, parent = None, text = '', file = None):
		tk.Frame.__init__(self, parent)

		self.pack(expand = tk.YES, fill = tk.BOTH) 
		self.make_widgets()
		self.set_text(text, file)
		
	def make_widgets(self):
		scrol_bar = tk.Scrollbar(self)
		text = tk.Text(self, relief = tk.SUNKEN, width = 30, height = 12)
		scrol_bar.config(command = text.yview)
		text.config(yscrollcommand = scrol_bar.set)
		
		scrol_bar.pack(side = tk.RIGHT, fill = tk.Y)
		text.pack(side = tk.LEFT, expand = tk.YES, fill = tk.BOTH)
		self.text = text
	
	def set_text(self, text = '', file = None):
		if file:
			text = open(file, 'r').read()
			
		self.text.delete('1.0', tk.END)
		self.text.insert('1.0', text)
		self.text.mark_set(tk.INSERT, '1.0')
		self.text.focus() # focus on text field
		
	def get_text(self):
		return self.text.get('1.0', tk.END+'-1c')
		
	
import sys

if __name__ == '__main__':
	root = tk.Tk()
	if len(sys.argv) > 1:
		st = Scroll_Text(file = sys.argv[1]) # file name is in command line
	else:
		st = Scroll_Text(text = 'Words\ngo here')
	
	def show(event):
		print(repr(st.get_text()) )
		
	root.bind('<Key-Escape>', show)
	root.mainloop()
