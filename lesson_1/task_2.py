# Задание 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in = int(input("Введите время в секундах: "))
time_s = time_in % 60
time_m = (time_in // 60) % 60
time_h = time_in // 60 // 60
print(f"Время = {time_h:02d}:{time_m:02d}:{time_s:02d}")
