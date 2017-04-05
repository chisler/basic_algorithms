graph = {
    "a": ["b", "c"],
    "b": [],
    "c": ["b"]
}

visited = {}


def search(current, end):
    if visited.get(current, False):
        return

    visited[current] = True

    if current == end:
        print("hooray")
        return

    for vertex in graph[current]:
        search(vertex, end)


search("b", "a")
