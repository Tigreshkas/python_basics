# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

odd_to_n = 15

num_gen = (num for num in range(1, odd_to_n + 1, 2))

print(*num_gen)
