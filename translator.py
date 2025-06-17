import morse
import morse_code

class Translator:
	
	# Преобразует звук в код Морзе
	def sound_to_code(self, audio):
		audio_array = audio.get_array_of_samples()
		audio_array_1 = morse.abs_lst(audio_array)
		audio_array_2 = morse.bin_list(audio_array_1)
			
		m = max(audio_array_1) # Максимальное значение
		sr = sum(audio_array_1)/len(audio_array_1) # Среднее значение
		sens =  sr/m # Чувствительность сигнала
		accur = 1 - (sens)**2
			
		lst_1 = morse.first_del_zeros(audio_array_2, accur)
		lst_2 = morse.trans_strlist_numlist(morse.second_del_zeros(lst_1, accur/2))
			
		lis = morse.seq_numbers(lst_2)
		#print(lis)
		lis_skelet = morse.struct_list(lst_2)
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
		
		return lst_2	
		

	# Преобразует символы кода Морзе в буквы 	
	def code_to_text(self, text):
		i = 1 # начинаем с первого элемента !!!
		m_text = text + '    '
		tmp = ''
		for i in range(len(m_text) - 1): # заканчиваем на один раньше!!!
		# удалить все  пробелы между точками и тире в букве
 		# если символ пробел 
			if m_text[i] == ' ' and m_text[i-1] !=' '  and m_text[i+1] != ' ':
				continue
			else: tmp += m_text[i] 
		#print(tmp)  # после удаления пробелов
		tmp += '        '
		
		message = '' # сообщение буквами
		i = 0
		symbol = '' # набор символов кода Морзе
		for i  in range(len(tmp) - 1):
		# если текущий не пробел
			if tmp[i] != ' ':
			 # добавить код в символ
				symbol += tmp[i]

				if tmp[i+1] == ' ': # следующий пробел, то конец символа 
			# сравнить со словарём и добавить в сообщение
					message += morse_code.c_abc[symbol]	
					# новая буква
					symbol = ''		
				continue		
				 
 		# если текущий пробел
#			if tmp[i] == ' ':
#					continue
						
		return message

					
if __name__ == '__main__':	
	text = ' . _  ._           _...                    _ . _ .    '
	print(text)
	
	t = Translator()
	print(t.code_to_text(text))
	
	
