
def apply_all_func(int_list, *functions):
    result = {}
    for function in functions: #перебор действий по списку, чтобы дальше применить это действие к числу
        res = function(int_list) # результат применения текущей функции из списка min, max, sum и тд
        func_name = function.__name__ # сохранение имени примененной функции
        result[func_name] = res # запись вышеописанных переменных в словарь
        # print(f"к списку{int_list} применена - {func_name}, результат:{res}")
    return result
# Пример использования:
print(apply_all_func([6, 20, 15, 9], min, max, sum))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))