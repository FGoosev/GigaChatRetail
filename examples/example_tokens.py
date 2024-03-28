"""Пример подсчета токенов в тексте"""
from gigachat import GigaChat

# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
from openpyxl import load_workbook
import time

wb = load_workbook(filename=r'/Users/fgoosev/Desktop/Ср-ва для депиляции классификатор.xlsx')
sheet_ranges = wb['AS IS']
bolName = False
sum = 0
avg = 0
min=500
max=0
count = 0
start = time.time()
for row in sheet_ranges:
    if bolName:
        count += 1
        with GigaChat(credentials="NmZhODY1ZjYtOWJiNy00ODcyLTkxNDEtYmUxZTdhMzgzOGY3OjJjNjZlNzg4LTYxYWYtNDdlMC1iODZhLTdkODk4OGQxZWI1Mw==",verify_ssl_certs=False) as giga:response = giga.chat("Что относится к этим параметрам товар, бренд, подбренд, группа, подгруппа, тип, цвет, вкус в названии \"%s\". Если параметр отсутствует в название, то не выводи его" % row[3].value)
        print(response.choices[0].message.content)
        totalTokens = int(response.usage.total_tokens)
        sum += totalTokens
        if min > totalTokens:
            min = totalTokens
        if max < totalTokens:
            max = totalTokens


    bolName = True
finish = time.time()
print('Сумма токенов потраченных на обработку Excel = %s' % sum)
print('Минимальное количество токенов = %s' % min)
print('Максимальное количество токенов = %s' % max)
print('Среднее количество токенов = %s' % (sum / count))
print('Время затраченное на весь запрос = %s' % (finish - start))