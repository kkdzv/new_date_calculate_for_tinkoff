from datetime import datetime, timedelta


def to_date_add_number (date: str, count_days: int) -> str:
    """
    Добавляет к дате указанное количество дней
    """
    try:
        parse_date = datetime.strptime(date, '%d.%m.%Y')
        new_date = parse_date + timedelta(days=count_days)


        return f'- К дате {date} было добавлено {count_days} суток.\n' \
               f'>>> Новая дата {new_date.strftime("%d.%m.%Y")} <<<'
    except ValueError:
        return f'>>> Ошибка. Дата указана с ошибкой'

