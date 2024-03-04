with open('referat.txt', 'r', encoding='utf-8') as f:
#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
	content = f.read()
	print(len(content))
#Замените точки в тексте на восклицательные знаки	
	a = content.replace('.', '!')
	print(a)
#Подсчитайте количество слов в тексте
	b = content
	c = content.split()
	d = len(c)
	print(d)
with open('referat2.txt', 'w', encoding='utf-8') as f2:
	referat2 = f2.write(a)
	print(referat2)