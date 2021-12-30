# Модуль с функцией поиска валюты и выдачи её курса
import requests


def currency_rates(currency):
    """The function of finding the exchange rate of a given currency"""
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')  # используем в качестве API ссылку
    content = resp.content.decode(encoding=resp.encoding)  # декодируем вышеуказанную страничку в понятный код
    for curr in currency:  # для значений в списке валют:
        if curr in content:  # проверяем, если валюта есть в коде, то выводим её курс
            for el in content.split(f'{curr}')[1:]:  # для элем. в строке, разделенной по элем., возьмем срез от 1 элем.
                cont = el.split('</Value>')[0]  # разделили строку по элементу и возьмём 0-й элемент
                for el_2 in cont.split('<Value>')[1:]:  # разделим строку по опред.элементу и возьмем срез от 1 элемента
                    print(float(el_2.replace(",", ".")))  # выводим значение как вещественное число
        else:  # иначе выводим "None"
            print('None')
