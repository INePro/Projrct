#СОЗДАЕМ ВЕЧНЫЙ ЦИКЛ
while True:
	#ОБВАРАЧИВАЕМ КОД В УСЛОВИЕ, ДЛЯ ИЗБЕЖАНИЯ ОШИБОК
	try:
		
		#ПРИСВАИВАЕМ ЗНАЧЕНИЯ ПЕРЕМЕННЫМ
		x_1 = int(input("Введите номер строки: "))
		y_1 = int(input("Введите номер столбца:"))
		x_2 = int(input("Введите номер строки: "))
		y_2 = int(input("Введите номер столбца:"))

		#abs - ЭТО МОДУЛЬ ЧИСЛА
		if abs(x_1 - x_2) == abs(y_1 - y_2):
		    print('YES')
		else:
		    print('NO')

	#ВЫВОД ТЕКСТА ПОДСКАЗКИ
	except ValueError:
		print("Нужно ввести целое число")
