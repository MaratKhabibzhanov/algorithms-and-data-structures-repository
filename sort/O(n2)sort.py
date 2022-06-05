def insertion_sort(rand_list):
    """Сортировка вставками"""
    for i in range(1, len(rand_list)):
        j = i
        while j > 0 and rand_list[j-1] > rand_list[j]:
            rand_list[j], rand_list[j-1] = rand_list[j-1], rand_list[j]
            j -= 1
    return rand_list


def selection_sort(rand_list):
    """Сортировка выбором"""
    n = len(rand_list)
    for i in range(n-1):
        for j in range(i+1, n):
            if rand_list[j] < rand_list[i]:
                rand_list[i], rand_list[j] = rand_list[j], rand_list[i]
    return rand_list


def bubble_sort(rand_list):
    """Пузырьковая сортировка"""
    n = len(rand_list)
    for i in range(n-1, 0, -1):
        flag = True
        for j in range(i):
            if rand_list[j] > rand_list[j+1]:
                rand_list[j], rand_list[j+1] = rand_list[j+1], rand_list[j]
                flag = False
        if flag:
            break
    return rand_list


insert_list = [2, 6, 8, 99, 340, 67, 7, 5, 6, 8, 22]
select_list = [2, 6, 8, 99, 340, 67, 7, 5, 6, 8, 22]
bubble_list = [2, 6, 8, 99, 340, 67, 7, 5, 6, 8, 22]
print(*insertion_sort(insert_list))
print(*selection_sort(select_list))
print(*bubble_sort(bubble_list))

