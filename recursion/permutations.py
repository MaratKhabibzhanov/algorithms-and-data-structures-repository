def generate_permitations(n, m=-1, prefix=None):
    """Генерация всех перестановок n чисел в m позициях, с префиксом prefix"""
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permitations(n, m-1, prefix)
        prefix.pop()


generate_permitations(5)