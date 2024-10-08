# 3.	Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы a и years,
# и возвращающую сумму, которая будет на счету пользователя

def bank(a, years):
    rate = 0.10  # процентная ставка
    for _ in range(years):
        a += a * rate  # увеличиваем вклад на 10% каждый год
    return a

# Пример использования функции:
initial_amount = float(input("Введите сумму вклада в рублях: "))
years = int(input("Введите количество лет: "))

final_amount = bank(initial_amount, years)
print(f"Сумма на счету после {years} лет будет равна {final_amount:.2f} руб.")

