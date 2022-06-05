def hoar_sort(rand_list):
    if len(rand_list) <= 1:
        return rand_list
    base_i = 0
    base_el = rand_list[base_i]
    for i in range(len(rand_list)):
        if rand_list[i] < rand_list[base_i]:
            el = rand_list.pop(i)
            rand_list.insert(base_i, el)
            base_i += 1
        elif rand_list[i] == rand_list[base_i] and i != base_i:
            rand_list.insert(base_i + 1, rand_list.pop(i))
    right_i = base_i + rand_list.count(base_el)
    return hoar_sort(rand_list[: base_i]) + rand_list[base_i: right_i] + \
           hoar_sort(rand_list[right_i:])


hoar_list = [80, 6, 8, 99, 340, 67, 80, 5, 6, 8, 22]
print(*hoar_sort(hoar_list))
