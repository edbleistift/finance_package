def annuity_payment(principal, rate, time):
    """
    Рассчитывает аннуитетный платеж (PMT).
    
    :param principal: Сумма кредита
    :param rate: Процентная ставка (в десятичной форме)
    :param time: Время в годах
    :return: Аннуитетный платеж

    Формула для расчета аннуитетного платежа:
    PMT = PV * (r * (1 + r)^t) / ((1 + r)^t - 1)
    
    где:
    PMT - аннуитетный платеж,
    PV - сумма кредита (principal),
    r - процентная ставка (rate),
    t - время в годах (time).
    """
    return principal * (rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)