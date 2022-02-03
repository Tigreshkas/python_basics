# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    def __str__(self):
        return f'{self.str_date}'

    @classmethod  # извлекает число, месяц, год и преобразовывает их тип к типу «Число»
    def class_int(cls, inform):
        str_date = str(inform)
        raw_str = str_date.split('-')
        month = {'янв': '01', 'фев': '02', 'мар': '03', 'апр': '04', 'мая': '05', 'июн': '06', 'июл': '07',
                 'авг': '08', 'сен': '09', 'окт': '10', 'ноя': '11', 'дек': '12'}
        dating = []
        if raw_str:
            dating.append(raw_str[0].zfill(2) if len(raw_str[0]) == 1 else raw_str[0])
            dating.append(month[raw_str[1][:3]]) if raw_str[1][:3] in month else dating.append('00')
            dating.append(raw_str[2])
        result = '-'.join(dating)
        return cls(result)

    @staticmethod  # проводит валидацию числа, месяца и года
    def stat_valid(obj):
        if obj.str_date:
            if int(obj.str_date[:2]) > 31 or int(obj.str_date[:2]) < 1:
                raise KeyError('Число введено неверно.')
            if not str(obj.str_date[:2]).isdigit():
                raise KeyError('Число введено неверно.')
            if int(obj.str_date[3:5]) == 00:
                raise KeyError('Месяц введен неверно.')
            if int(obj.str_date[6:]) > 10000:
                raise KeyError('Год введен неверно.')
            return f'{obj.str_date} Формат даты верный'


date_1 = Date('5-декабря-2021')
print(date_1.class_int(date_1))
print(date_1.stat_valid(Date.class_int(date_1)))
