def merge_sort(rand_list):
    if len(rand_list) <= 1:
        return rand_list
    mid_i = len(rand_list) // 2
    left_list = merge_sort(rand_list[:mid_i])
    right_list = merge_sort(rand_list[mid_i:])
    i, j = 0, 0
    rand_list.clear()
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            rand_list.append(left_list[i])
            i += 1
        else:
            rand_list.append(right_list[j])
            j += 1
    if i < len(left_list):
        rand_list.extend(left_list[i:])
    else:
        rand_list.extend(right_list[j:])
    return rand_list


merge_list = [80, 6, 8, 99, 340, 67, 80, 5, 6, 8, 22]
print(*merge_sort(merge_list))
