def future_value(principal, rate, time):
    """
    Рассчитывает будущую стоимость (FV).
    
    :param principal: Начальная сумма
    :param rate: Процентная ставка (в десятичной форме)
    :param time: Время в годах
    :return: Будущая стоимость

    Формула для расчета будущей стоимости:
    FV = PV * (1 + r) ^ t
    
    где:
    FV - будущая стоимость,
    PV - начальная сумма (principal),
    r - процентная ставка (rate),
    t - время в годах (time).
    """
    return principal * (1 + rate) ** time