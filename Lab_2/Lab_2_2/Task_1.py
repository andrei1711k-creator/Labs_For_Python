def make_flat_list(lst):

    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):

            sublist = lst[i]
            make_flat_list(sublist)

            lst[i:i + 1] = sublist
            i += len(sublist)
        else:
            i += 1


if __name__ == "__main__":
    list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
    print(f"Исходный список: {list_a}")

    make_flat_list(list_a)
    print(f"Плоский список: {list_a}")