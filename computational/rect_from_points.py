def hash(p1, p2):
    if p1 < p2:
        p1, p2 = p2, p1

    return ".".join(str(i) for i in (p1 + p2))


def rect(points):
    def get_mixed(p1, p2):
        return (p1[0], p2[1]), (p2[0], p1[1])

    lookup = set(points)
    rects = set()

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue

            p3, p4 = get_mixed(p1, p2)

            if p3 in (p1, p2) or p4 in (p1, p2):
                continue

            if p3 in lookup and p4 in lookup:
                rects.add(hash(p1, p2))


    return len(rects) / 2


print(rect([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 2), (1, 2)]))
