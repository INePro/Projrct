#СОЗДАЕМ ВЕЧНЫЙ ЦИКЛ
while True:
	#ОБВАРАЧИВАЕМ КОД В УСЛОВИЕ, ДЛЯ ИЗБЕЖАНИЯ ОШИБОК
	try:
		
		n = int(input("Введите число: "))
		if n == 0:
		    print(0)
		else:
		    chisl_1 = 0
		    chisl_2 = 1
		    #range(старт, стоп, шаг)
		    for i in range(2, n + 1):
		        chisl_1, chisl_2 = chisl_2, chisl_1 + chisl_2 #Сокращенная запись
		    print(chisl_2)

	#ВЫВОД ТЕКСТА ПОДСКАЗКИ
	except ValueError:
		print("Вводите корректные данные!")
