# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

odd_to_n = 15


def num_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


print(*num_gen(odd_to_n))
