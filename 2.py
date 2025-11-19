''' структура 3 числа ввод проверить какой треугольник прямоугольный остроугольный тупогольный'''


def dec_file(func):
    def wrapper(a):
        result = func(a)
        with open("file_test_2.txt","a",encoding="utf-8") as f:
            f.write(f"{result} \n")
        return result
    return wrapper


@dec_file
def type_of_triangle(a):

    arr = a.split()


    arr[1] = int(arr[1])
    arr[2] = int(arr[2])
    arr[0] = int(arr[0])
    max_el = max(arr)

    arr_1 = arr.copy()
    arr_1.remove(max(arr_1))




    if max_el >= (arr_1[0]+arr_1[1]):
        print(f"треугольника со сторонами {arr[0]} {arr[1]} {arr[2]} не существует")
        return (f"треугольника со сторонами {arr[0]} {arr[1]} {arr[2]} не существует")


    if max_el**2 ==(arr_1[0]**2+ arr_1[1]**2):
        print(f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]} прямоугольный ")

        return (f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]} прямоугольный ")


    if max_el ** 2 > (arr_1[0]** 2 + arr_1[1] ** 2):
        print(f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]}  тупоугольный")

        return (f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]}  тупоугольный")


    if max_el ** 2 < (arr_1[0]** 2 + arr_1[1] ** 2):
        print(f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]}  остроугольный")

        return (f"треугольник со сторонами {arr[0]} {arr[1]} {arr[2]}  остроугольный")


while True:
  a = input('введите стороны треугольников:')
  if a.lower()== "стоп мне не приятно":
     break
  else: type_of_triangle(a)