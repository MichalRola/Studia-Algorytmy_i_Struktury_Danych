class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


def orientation(p, q, r):
    value = (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x)
    # jeżeli (p, q, r) jest prawoskrętne
    if value > 0:
        return 0
    # jeżeli (p, q, r) jest lewoskrętne
    elif value < 0:
        return 1
    # jeżeli (p, q, r) jest współliniowe
    else:
        return 2


def is_between(p, q, r):
    return q.x >= min(p.x, r.x) and q.x <= max(p.x, r.x) and q.y >= min(p.y, r.y) and q.y <= max(p.y, r.y)


def jarvis_algorithm(lst, check_q=True):
    score_lst = []
    p = 0
    for point in range(len(lst)):
        if lst[p].x > lst[point].x:
            p = point
        elif lst[p].x == lst[point].x:
            if lst[p].y > lst[point].y:
                p = point
    left_most_point = p
    while True:
        score_lst.append(lst[p])

        q = (p + 1) % len(lst)

        for r in range(len(lst)):
            if orientation(lst[p], lst[q], lst[r]) == 0:
                q = r
            
            if check_q is True and orientation(lst[p], lst[r], lst[q]) == 2 and is_between(lst[p], lst[q], lst[r]):
                q = r
        p = q
        if p == left_most_point:
            break
    return score_lst


data = (2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)
lst = [Point(elem[0], elem[1]) for elem in data]

# Wynik bez sprawdzania czy q jest najdalszym współliniowym punktem.
result_1 = jarvis_algorithm(lst, False)
print(result_1)
# Wynik ze sprawdzaniem czy q jest najdalszym współliniowym punktem.
result_2 = jarvis_algorithm(lst)
print(result_2)
