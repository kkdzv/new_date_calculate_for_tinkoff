import re


def parse_date(user_date: str) -> str:
    """
    Ищет дату в строке. Заменяет символ между ДД-ММ-ГГГГ на корректный
    """
    change_symbols = ''.join(re.findall(r'\d{2}.\d{2}.\d{4}', user_date))
    result = re.sub(r'[^0-9]', '.', change_symbols)

    return result