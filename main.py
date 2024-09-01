# 1.	Напишите функцию sum_range(start, end), которая суммирует все целые числа
# от значения start до величины end включительно


def summ_range(start, end):
    summ = 0
    for i in range(start, end + 1):
        summ += i
    return summ
start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

summ_range(start, end)

print(summ_range(start, end))