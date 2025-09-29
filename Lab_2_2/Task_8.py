import time


def timing(func):


    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()

        delta_time = (finish_time - start_time) *  1000
        print(f"Функция {func.__name__} выполнилась за {delta_time} мс")

        return result

    return wrapper


if __name__ == "__main__":

    @timing
    def test_1(n):

        result = 0
        for i in range(n):
            for j in range(n):
               for z in range(n):
                   result += i + j +z
        return result


    @timing
    def test_2(n):

        return n**2



    print("Тестирование замера времени:")
    result1 = test_1(500)
    result2 = test_2(1000000)
    print(f"1ый тест: {result1}")
    print(f"2ой тест: {result2}")