from decorators import log_decorator_with_param

@log_decorator_with_param('get_employees_log.txt')
def get_employees():
    return 'Выполнена функция get_employees'