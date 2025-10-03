import time


def log_calls(file_name):


    def decorator_func(some_func):
        def inner_function(*some_args, **some_kwargs):
            current_time_var = time.strftime("%Y-%m-%d %H:%M:%S")

            list_for_args = []

            for argument in some_args:
                string_arg = str(argument)
                list_for_args.append(string_arg)
            args_string_result = ", ".join(list_for_args)

            list_for_kwargs = []


            for k, v in some_kwargs.items():

                value_as_string = str(v)
                kwarg_string_format = f"{k}={value_as_string}"
                list_for_kwargs.append(kwarg_string_format)
            kwargs_string_result = ", ".join(list_for_kwargs)

            combined_args_list = [args_string_result, kwargs_string_result]
            filtered_args = []
            for s in combined_args_list:
                if s:
                    filtered_args.append(s)

            final_args_string = ", ".join(filtered_args)

            with open(file_name, 'a', encoding='utf-8') as file_obj:
                file_obj.write(f"{current_time_var} - {some_func.__name__}({final_args_string})\n")

            return some_func(*some_args, **some_kwargs)

        return inner_function

    return decorator_func


if __name__ == "__main__":

    @log_calls("log_file.txt")
    def add(a, b):
        return a + b

    res_1 = add(5, 3)
    res_2 = add(10, 20, text="something")
    print(f"Первый результат: {res_1}")
    print(f"Второй результат: {res_2}")
    print("Данные записаны в файл 'log_file.txt'")