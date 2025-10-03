def type_check(*req_types):


    def decorator(func):
        def wrapper(*args, **kwargs):

            for i in range(len(args)):

                arg = args[i]

                if i < len(req_types):
                    req_type = req_types[i]

                    if not isinstance(arg, req_type):
                        raise TypeError(f"Аргумент {i} должен быть типа {req_type.__name__}, а получен {type(arg).__name__}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == "__main__":

    @type_check(int, int)
    def add(a, b):
        return a + b


    @type_check(str, int)
    def mult_string(a, b):
        return a * b



    try:
        result1 = add(5, 3)
        print(f"add(5, 3) = {result1}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        result2 = mult_string("hello", 3)
        print(f"add_string('hello', 3) = {result2}")
    except TypeError as e:
        print(f"Ошибка: {e}")


    try:
        result3 = add("5", 3)
        print(f"add('5', 3) = {result3}")
    except TypeError as e:
        print(f"Ошибка: {e}")