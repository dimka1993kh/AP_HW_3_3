from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    # print('Запущено из main')
    calculate_salary = calculate_salary()
    # print(calculate_salary)
    get_employees = get_employees()
    # print(get_employees)
    # print(datetime.now())
