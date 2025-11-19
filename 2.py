''' структура 3 числа ввод проверить какой треугольник прямоугольный остроугольный тупогольный'''
d =1


def type_of_triangle(a):

    arr = a.split()


    arr[1] = int(arr[1])
    arr[2] = int(arr[2])
    arr[0] = int(arr[0])
    max_el = max(arr)
    print(max_el)
    arr_1 = arr
    arr_1.remove(max(arr_1))




    if max_el >= (arr_1[0]+arr_1[1]):
        with open('test_2.txt','w',encoding="utf-8") as f:
            f.write(f"треугольника со сторонами {arr[0]} {arr[1]} {max_el} не существует")


    if max_el**2 ==(arr_1[0]**2+ arr_1[1]**2):
        with open('test_2.txt','w',encoding="utf-8") as f:
            f.write(f"треугольник со сторонами {arr[0]} {arr[1]} {max_el} прямоугольный ")


    if max_el ** 2 > (arr_1[0]** 2 + arr_1[1] ** 2):
        with open('test_2.txt', 'w',encoding="utf-8") as f:
            f.write(f"треугольник со сторонами {arr[0]} {arr[1]} {max_el}  тупоугольный")


    if max_el ** 2 < (arr_1[0]** 2 + arr_1[1] ** 2):
        with open('test_2.txt', 'w',encoding="utf-8") as f:
            f.write(f"треугольник со сторонами {arr[0]} {arr[1]} {max_el}  остроугольный")


while d:
  a = input('введите стороны треугольников:')
  if a == "я наигрался(лась)":
     d =0
  else: type_of_triangle(a)



