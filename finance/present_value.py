def present_value(future_value, rate, time):
    """
    Рассчитывает приведенную стоимость (PV).
    
    :param future_value: Будущая стоимость
    :param rate: Процентная ставка (в десятичной форме)
    :param time: Время в годах
    :return: Приведенная стоимость

    Формула для расчета приведенной стоимости:
    PV = FV / (1 + r) ^ t
    
    где:
    PV - приведенная стоимость,
    FV - будущая стоимость (future_value),
    r - процентная ставка (rate),
    t - время в годах (time).
    """
    return future_value / (1 + rate) ** time