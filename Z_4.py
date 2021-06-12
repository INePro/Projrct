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
		modul_x = abs(x_1 - x_2)
		modul_y = abs(y_1 - y_2)

		if modul_x == 1 and modul_y == 2 or modul_x == 2 and modul_y == 1:

		    print('YES')
		else:
		    print('NO')

	#ВЫВОД ТЕКСТА ПОДСКАЗКИ
	except ValueError:
		print("Нужно ввести целое число")
