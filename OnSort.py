def counting_sort(in_list, notation):
    frequency = [0] * notation
    out_list = list()
    for i in in_list:
        frequency[i] += 1
    for digit in range(notation):
        count = frequency[digit]
        for _ in range(count):
            out_list.append(digit)
    return out_list


counting_list = [2, 6, 8, 9, 3, 6, 7, 5, 6, 8, 2, 6, 4, 3, 6, 9, 0, 1, 2, 6, 3]
print(*counting_sort(counting_list, 10))
