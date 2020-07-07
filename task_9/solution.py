def is_palindrome(x: int) -> bool:
    """
    Дано число. Необходимо узнать, является ли это число палиндромом.

    Примеры:
    121 - true,
    -121 - false
    10 - false

    Args:
        x: исходное число

    Returns: булево значение, означающее результат проверки

    """
    if x < 0:
        return False

    y = 0
    num = x
    while num > 0:
        y *= 10
        y += num % 10
        num //= 10

    return x == y
