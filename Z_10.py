#СОЗДАЕМ ВЕЧНЫЙ ЦИКЛ
while True:
	#ОБВАРАЧИВАЕМ КОД В УСЛОВИЕ, ДЛЯ ИЗБЕЖАНИЯ ОШИБОК
	try:
		chisl_1 = int(input("Введите первое число: "))
		chisl_2 = int(input("Введите второе число: "))

		#CРАВНИВАЕМ ЧИСЛА И ЗАДАЕМ УСЛОВИЯ
		if chisl_1 < chisl_2:
			# range(старт, стоп)
		    for i in range(chisl_1, chisl_2 + 1):
		        print(i)
		else:
			#range(старт, стоп, шаг)
		    for i in range(chisl_1, chisl_2 - 1, -1): # шаг в -1 позволяет выводить числа в порядке убывания
		        print(i)

	#ВЫВОД ТЕКСТА ПОДСКАЗКИ
	except ValueError:
		print("Нужно ввести целое число")
