from finance.future_value import future_value
from finance.present_value import present_value
from finance.annuity import annuity_payment
from finance.rate import calculate_rate


principal = float(input("Введите начальную сумму (Principal): "))
rate = float(input("Введите процентную ставку в виде десятичной дроби (например, 0.05 для 5%): "))
time = int(input("Введите количество лет (Time): "))

# Рассчитываем будущую стоимость (Future Value)
fv = future_value(principal, rate, time)

# Рассчитываем приведенную стоимость (Present Value) на основе будущей стоимости
pv = present_value(fv, rate, time)

# Рассчитываем аннуитетный платеж (Annuity Payment) на основе начальной суммы, ставки и времени
pmt = annuity_payment(principal, rate, time)

# Рассчитываем процентную ставку на основе будущей стоимости и начальной суммы
calculated_rate = calculate_rate(fv, principal, time)

print("\n================ Финансовые расчеты ================\n")
print(f"Начальная сумма (Principal): {principal}")
print(f"Процентная ставка (Rate): {rate * 100:.2f}%")
print(f"Количество лет (Time): {time} лет\n")

print("----------- Результаты расчетов -----------")
print(f"\n Будущая стоимость (FV): {fv:.2f}")
print(f"  Будущая стоимость через {time} лет при процентной ставке {rate * 100:.2f}% и начальной сумме {principal}.")

print(f"\n Приведенная стоимость (PV): {pv:.2f}")
print(f"  Приведенная стоимость на данный момент для будущей стоимости {fv:.2f} через {time} лет.")

print(f"\n Аннуитетный платеж (PMT): {pmt:.2f}")
print(f"  Чтобы покрыть начальную сумму {principal} с процентной ставкой {rate * 100:.2f}% за {time} лет, вы должны вносить {pmt:.2f} ежегодно.")

print(f"\n Рассчитанная процентная ставка (Rate): {calculated_rate:.2f}")
print(f"  Процентная ставка, которая приводит начальную сумму {principal} к будущей стоимости {fv:.2f} за {time} лет.\n")

print("======================================================")