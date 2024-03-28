from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import time


start = time.time()
# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.USER,
            content="\"AXE Signature Антип/стик против бел след муж50мл(Юнилевер):6\" преобразуй в полное название. Выдели из результата атрибуты и подпиши их"
        )
    ],
    temperature=0.1,
    max_tokens=500,
)
with GigaChat(credentials="NmZhODY1ZjYtOWJiNy00ODcyLTkxNDEtYmUxZTdhMzgzOGY3OjJjNjZlNzg4LTYxYWYtNDdlMC1iODZhLTdkODk4OGQxZWI1Mw==", verify_ssl_certs=False) as giga:
    response = giga.chat(payload)
    print(response.choices[0].message.content)
finish = time.time()
print('Время работы: ' + str(finish - start))

# from openpyxl import load_workbook
# wb = load_workbook(filename=r'/Users/fgoosev/Desktop/Ср-ва для депиляции классификатор.xlsx')
# sheet_ranges = wb['AS IS']
# for row in sheet_ranges:
#     print(row[3].value)
#     break