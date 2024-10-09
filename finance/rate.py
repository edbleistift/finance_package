def calculate_rate(future_value, principal, time):
    """
    Рассчитывает процентную ставку (Rate).
    
    :param future_value: Будущая стоимость
    :param principal: Начальная сумма
    :param time: Время в годах
    :return: Процентная ставка

    Формула для расчета процентной ставки:
    r = (FV / PV)^(1/t) - 1
    
    где:
    r - процентная ставка,
    FV - будущая стоимость (future_value),
    PV - начальная сумма (principal),
    t - время в годах (time).
    """
    return (future_value / principal) ** (1 / time) - 1