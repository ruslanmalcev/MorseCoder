# Порядок единиц и нулей
def struct_list(lst):
	mas = seq_numbers(lst)
	skelet = []
	if lst[0] == 0:
		skelet = [0,1]*(len(mas)//2+1)
	else:
		skelet = [1,0]*(len(mas)//2+1)
	
	if len(skelet)>len(mas):
		res = skelet[0:len(mas)]
	else:
		res = skelet
	return res
	
# Список из положительных значений
def abs_lst(lst):
	result = []
	for i in range(len(lst)):
		if lst[i]<0:
			result.append(lst[i]*(-1))
		else:
			result.append(lst[i])
	return result

# Список состоящий только из единиц и нулей, где каждое значение удовлетворяет условию	
def bin_list(lst):
	result = []
	m = max(lst)
	sr = sum(lst)/len(lst)
	accur = sr/m # "Чувствительность сигнала"
	for i in range(len(lst)):
		if lst[i]/m >= accur:
			result.append(1)
		else:
			result.append(0)
	return result

"""
Функция для подсчёта количества чисел повторяющегося числа
в непрерывной последовательности, остальные элементы заменяются нулями
"""
def count_numbers(lst, num):
	res1 = []
	count1 = 0
	for i in range(len(lst)):
		if lst[i]==num:
			count1 += 1
		else:
			res1.append(count1)
			count1 = 0
	res11 = []
	for i in range(len(res1)):
		if res1[i]!=num:
			res11.append(res1[i])
	return res1

"""
Функция считает количество последовательных нулей и единиц
на выходе выдает список чисел, кажды элемент которого равен числу либо
нулей либо единиц.
"""
def seq_numbers(lst):
	res = []
	itr = 0
	lim = 0
	while lim!=len(lst):
		for i in range(lim, len(lst)):
			number = lst[lim]
			if lst[i] == number:
				itr+=1
			else:
				break
		lim += itr
		res.append(itr)
		itr = 0
	return res


""" 
Заменяет незначащие нули и переводит список чисел в список, состоящий
из повторяющихся единиц и нулей. С сохранением длины списка
"""
def first_del_zeros(lst, accur):
	mas = seq_numbers(lst)+[1] # Добавляем один элемент, чтобы сохранить размер списка
	alphabet = struct_list(lst)
	result = []
		
	for i in range(0, len(mas)-1):
		if mas[i]/mas[i+1] <= accur:
			#result += [alphabet[i+1]]*mas[i+1]
			result += [alphabet[i+1]]*mas[i]
		else:
			result += [alphabet[i]]*mas[i]
	return result
	
# Убирает помехи
def second_del_zeros(lst, accur):
	y = seq_numbers(lst)+[1]
	res = []
	alph = struct_list(lst)
	res.append(str(alph[0])*y[0])
	for i in range(1,len(y)-1):
		if alph[i] == 0:
			ratio = y[i]/(len(res[-1])+y[i+1])
			if ratio/(1/6) >= accur or ratio/(1/4) >= accur:
				res.append(str(alph[i])*(y[i]))
			else:
				res[-1]+=(str(alph[i+1])*y[i])
		else:
			if res[-1][0]=='1':
				res[-1]+=(str(alph[i])*y[i])
			else:
				res.append(str(alph[i])*y[i])

	return(res)

# Переводит список, состоящий из строк, в список из чисел
def trans_strlist_numlist(lst):
	string = ''
	result = []
	for i in range(len(lst)):
		string += lst[i]
	for i in range(len(string)):
		result.append(int(string[i]))
	return(result)
