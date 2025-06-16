import matplotlib.pyplot as plt

def graf_plot(lst):
	time_audio = [i for i in range(0,len(lst))]
	plt.plot(time_audio, lst)
	return plt.show()
