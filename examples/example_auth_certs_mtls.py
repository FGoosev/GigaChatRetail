"""Взаимная аутентификация по протоколу TLS (mTLS)"""

from gigachat import GigaChat
import time

start = time.time()
# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
with GigaChat(temperature=0.1,credentials="NmZhODY1ZjYtOWJiNy00ODcyLTkxNDEtYmUxZTdhMzgzOGY3OjJjNjZlNzg4LTYxYWYtNDdlMC1iODZhLTdkODk4OGQxZWI1Mw==", verify_ssl_certs=False) as giga:
    response = giga.chat("\"AXE Signature Антип/стик против бел след муж50мл(Юнилевер):6\" преобразуй в полное название. Выдели из результата атрибуты и подпиши их")
    print(response.choices[0].message.content)
finish = time.time()
print('Время работы: ' + str(finish - start))
