def unique_elements(nested_list):

    result = []

    def ext_elements(lsts):

        for part in lsts:
            if isinstance(part, list):
                ext_elements(part)
            else:
                if part not in result:
                    result.append(part)

    ext_elements(nested_list)
    return result


if __name__ == "__main__":

    list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]

    print(f"Исходный список : {list_a}")

    unique_list = unique_elements(list_a)
    print(f"Униккальные элементы: {unique_list}")