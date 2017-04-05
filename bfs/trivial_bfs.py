from collections import deque

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "d": ["e"],
    "c": ["e"]
}

visited = {}

path = {}


def search(start, end):
    stack = deque()

    stack.append((start, None))

    while stack:
        current, prev = stack.popleft()
        path[current] = prev

        if not visited.get(current, False):
            visited[current] = True

            if current == end:
                print("hooray")
                return

            for v in graph[current]:
                stack.append((v, current))


def get_path(start, end):
    reversed_path = []

    while end != start:
        reversed_path.append(end)
        end = path[end]

    reversed_path.append(start)
    return list(reversed(reversed_path))


search("a", "e")
print(get_path("a", "e"))
