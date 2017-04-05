from collections import deque

# No cycles
graph1 = {
    "1": ["4"],
    "4": ["2", "3"],
    "2": [],
    "3": ["2"]
}

# Cycle here
graph2 = {
    "a": ["b"],
    "b": ["a"]
}


class Color(object):
    WHITE = 1
    GREY = 2
    BLACK = 3


def topologicat_sort(graph):
    order = deque()
    colors = {}

    def search(current):
        colors[current] = Color.GREY

        for vertex in graph[current]:
            vertex_color = colors.get(vertex, Color.WHITE)

            if vertex_color == Color.GREY:
                raise ValueError("Cycle here")

            if vertex_color == Color.BLACK:
                continue

            if vertex_color == Color.WHITE:
                search(vertex)

        colors[current] = Color.BLACK
        order.append(current)
        return

    first_item = next(iter(graph))
    search(first_item)
    return order


def dfs(graph):
    order = deque()
    stack = deque()

    first_item = next(iter(graph))
    order.append(first_item)
    colors = {}

    while order:
        c = order.pop()
        if not colors.get(c):
            stack.append(c)
            colors[c] = Color.GREY

            for child in graph[c]:
                child_color = colors.get(child)

                if child_color is None:
                    order.append(child)

                if child_color == Color.GREY:
                    raise ValueError("Cycle")

    return stack


print(topologicat_sort(graph1))
# print(topologicat_sort(graph2))

print(dfs(graph1))
# print(dfs(graph2))
