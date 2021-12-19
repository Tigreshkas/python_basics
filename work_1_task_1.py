# Перевод секунд в сутки, часы, минуты и секунды
duration = int(input('Введите секунды: '))

if duration < 60:
    print(f'{duration} сек')
elif duration < 3600:
    print(f'{duration // 60} мин {duration % 60} сек')
elif duration < 86400:
    hour = duration // 3600
    minute = (duration - hour*3600) // 60
    second = (duration - hour*3600 - minute*3600) % 60
    print(f'{hour} час {minute} мин {second} сек')
elif duration >= 86400:
    day = duration // 86400
    hour = (duration - day*86400) // 3600
    minute = (duration - day*86400 - hour*3600) // 60
    second = (duration - day*86400 - hour*3600 - minute*60) % 60
    print(f'{day} дн {hour} час {minute} мин {second} сек')
