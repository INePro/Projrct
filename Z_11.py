#СОЗДАЕМ ВЕЧНЫЙ ЦИКЛ
while True:
	#ОБВАРАЧИВАЕМ КОД В УСЛОВИЕ, ДЛЯ ИЗБЕЖАНИЯ ОШИБОК
	try:
		chisl = 1
		n = int(input("Введите целое натуральное число: "))
		for i in range(1, n + 1):
		    chisl = chisl * i
		print(chisl)

	#ВЫВОД ТЕКСТА ПОДСКАЗКИ
	except ValueError:
		print("Нужно ввести целое число")
