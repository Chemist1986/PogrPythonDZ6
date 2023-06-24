import sys
from datetime import datetime

def check_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите дату в формате ГГГГ-ММ-ДД")
    else:
        date_to_check = sys.argv[1]
        if check_date(date_to_check):
            print("Дата {} действительна!".format(date_to_check))
        else:
            print("Дата {} недействительна!".format(date_to_check)) # Для проверки необходимо удалить "-"
