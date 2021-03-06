from collections import deque

# graph = {
#     "a": ["c"],
#     "b": ["a", "c"],
#     "c": ["d"],
#     "d": []
# }

graph = {
    "a": ["c", "e", "b"],
    "b": ["d"],
    "d": ["e"],
    "c": ["e"]
}

visited = {}

path = {}


def search(start, end):
    stack = deque()

    stack.append(start)

    while stack:
        current = stack.pop()
        if not visited.get(current):
            visited[current] = True

            if current == end:
                print("hooray")
                return

            for v in graph[current]:
                    path[v] = current
                    stack.append(v)


def get_path(start, end):
    reversed_path = []

    while end != start:
        reversed_path.append(end)
        end = path[end]

    reversed_path.append(start)
    return list(reversed(reversed_path))


search("a", "e")
print(get_path("a", "e"))
