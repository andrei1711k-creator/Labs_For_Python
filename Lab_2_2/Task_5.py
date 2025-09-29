def cache(func):

    cache_dict = {}

    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))


        if key in cache_dict:
            print(f"Возвращаем результат из кэша для {func.__name__}{args}")
            return cache_dict[key]


        result = func(*args, **kwargs)
        cache_dict[key] = result
        print(f"Вычислен новый результат для {func.__name__}{args}")

        return result

    return wrapper


if __name__ == "__main__":

    @cache
    def add_numbers(a, b):


        return a + b

    @cache
    def mult(a, b):
        return a * b



    print("Сложение чисел:")
    print(f"add_numbers(5,10) = {add_numbers(5,10)}")

    print("\nУмножение:")
    print(f"mult(3, 4) = {mult(3, 4)}")
