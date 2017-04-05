graph = {
    "a": ["c"],
    "b": ["a", "c"],
    "c": ["d"],
    "d": []
}

visited = {}

path = {}


def search(current, end):
    visited[current] = True

    if current == end:
        print("hooray")
        return

    for vertex in graph[current]:
        if not visited.get(vertex, False):
            path[vertex] = current
            search(vertex, end)


def get_path(start, end):
    reversed_path = []

    while end != start:
        reversed_path.append(end)
        end = path[end]

    reversed_path.append(start)
    return list(reversed(reversed_path))


search("b", "d")
print(get_path("b", "d"))
