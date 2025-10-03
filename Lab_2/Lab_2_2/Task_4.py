def trans_matrix(matrix):


    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])


    trans = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        trans.append(new_row)

    return trans


if __name__ == "__main__":

    print("Введите матрицу построчно:")

    matrix = []
    while True:
        row_input = input().strip()
        if not row_input:
            break
        row = []
        sp_result = row_input.split()
        for x in sp_result:
            number = int(x)
            row.append(number)
        matrix.append(row)

    print(f"\nИсходная матрица:")
    for row in matrix:
        print(row)

    trans = trans_matrix(matrix)

    print(f"\nТранспонированная матрица:")
    for row in trans:
        print(row)