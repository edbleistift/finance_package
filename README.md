# Пакет для финансовых расчетов

Этот пакет предоставляет функции для расчета различных финансовых показателей, таких как:
- Будущая стоимость (FV)
- Приведенная стоимость (PV)
- Аннуитетные платежи (PMT)
- Процентная ставка (Rate)

# Установка

## Шаг 1: Клонирование репозитория

Для начала склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/edbleistift/finance_package.git
cd finance-package
```
 
## Шаг 2: Создание и активация виртуального окружения (рекомендуется)
Рекомендуется использовать виртуальное окружение для управления зависимостями: 

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```

## Шаг 3: Установка пакета
Инсталируйте инструменты для установки пакета:

```bash
pip install setuptools
```

Находясь в папке проекта, выполните следующую команду для установки пакета и его зависимостей:
```bash
pip install .
```

## Шаг 4: Проверка установки
Чтобы убедиться, что пакет установлен, выполните:

```bash
pip list
```

# Использование
После установки вы можете импортировать и использовать пакет в своем коде Python:

```bash
from finance.future_value import future_value
from finance.present_value import present_value
from finance.annuity import annuity_payment
from finance.rate import calculate_rate

# Пример использования
principal = 1000
rate = 0.05
time = 10

fv = future_value(principal, rate, time)
pv = present_value(fv, rate, time)
pmt = annuity_payment(10000, rate, time)
r = calculate_rate(fv, principal, time)

print(f"Будущая стоимость: {fv}")
print(f"Приведенная стоимость: {pv}")
print(f"Аннуитетный платеж: {pmt}")
print(f"Процентная ставка: {r}")
```