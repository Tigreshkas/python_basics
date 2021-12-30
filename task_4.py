# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates()

from utils import currency_rates  # Импортирую только функию currency_rates из модуля utils

# exchange = input('Введите код валюты или коды валют (через запятую): ')  # для ручного ввода валют
exchange = 'eur, Gbp, BGN, jjdf, usd'  # проверяем несколько значений (от регистра не зависит)
exchange_list = exchange.upper().split(', ')  # разделим строку по "," и сделаем все буквы большими
currency_rates(exchange_list)  # выводим результат функции
