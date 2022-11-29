from parse_date import parse_date
from to_date_add_number import to_date_add_number


def main() -> str:
    try:
        user_date = str(input("Укажи дату, к которой нужно прибавить дни,\n"
                              "(формат даты должен быть следующий - ДД:ММ:ГГГГ): "))
        how_many_days = int(input("Сколько суток добавить к дате? (Введите целое число): "))
    except ValueError:
        return ">>> Ошибка. Дата / Количество суток указаны в неправильном формате.\n" \
               ">>> Следуй подсказкам в скобках"

    return to_date_add_number(parse_date(user_date), count_days=how_many_days)


if __name__ == "__main__":
    print(main())