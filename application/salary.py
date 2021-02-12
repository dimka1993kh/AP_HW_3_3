from decorators import log_decorator_with_param

@log_decorator_with_param('calculate_salary_log.txt')
def calculate_salary():
    return 'Выполнена функция calculate_salary'