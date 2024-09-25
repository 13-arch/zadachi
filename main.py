'''ыведите в выходной файл округленное до n знаков после десятичной 
точки число 
E. В данной задаче будем считать, что число Е в точности равно 
2.7182818284590452353602875.

Входные данные
Входной файл INPUT.TXT содержит целое число n (0 ≤ n ≤ 25).

Выходные данные
В выходной файл OUTPUT.TXT выведите ответ на задачу.'''
from decimal import Decimal
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')


number = Decimal("2.7182818284590452353602875")
a = int(data)


Reselt = round(number , a)
output_data.write(str(Reselt))
input_data.close
output_data.close