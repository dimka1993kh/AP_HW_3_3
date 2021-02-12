from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    # print('Запущено из dirty_main')
    calculate_salary = calculate_salary()
    # print(calculate_salary)
    get_employees = get_employees()
    # print(get_employees)
    # print(datetime.now())