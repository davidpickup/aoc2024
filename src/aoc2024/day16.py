import heapq

def _draw_path(maze: list[list[str]], route: list[tuple[int, int, int, int]]) -> str:
    """Draw the path on the maze."""
    for i, j, dx, dy in route:
        if maze[i][j] not in "SE":
            if dx == 0 and dy == 1:
                maze[i][j] = ">"
            elif dx == 0 and dy == -1:
                maze[i][j] = "<"
            elif dx == 1 and dy == 0:
                maze[i][j] = "v"
            elif dx == -1 and dy == 0:
                maze[i][j] = "^"
    return "\n".join("".join(row) for row in maze)

def _shortest_path(maze: list[list[str]], heap: list[tuple[int, tuple[int, int]]], adjacency_list: dict) -> int:
    """Find the shortest path from S to E."""
    visited = set()
    on_route = set()
    lowest_cost = float("inf")
    while heap:
        cost, (node, route) = heapq.heappop(heap)
        i, j, dx, dy = node
        if node in visited or cost > lowest_cost:
            if (i, j, dx, dy, cost) in on_route:
                on_route = on_route | set(route)
            continue
        visited.add(node)
        if maze[i][j] == "E":
            lowest_cost = cost
            on_route = on_route | set(route)
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                ndx, ndy = neighbour[2], neighbour[3]
                if dx != ndx or dy != ndy:
                    heapq.heappush(heap, (cost + 1000, (neighbour, route + [(i, j, ndx, ndy, cost+1000)])))
                else:
                    heapq.heappush(heap, (cost + 1, (neighbour, route + [(i, j, ndx, ndy, cost+1)])))
    return lowest_cost, visited, on_route

def _build_adjacency_list(maze: list[list[str]]) -> dict:
    """Build an adjacency list for the maze."""
    adjacency_list = {}
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != "#":
                for di, dj in directions:
                    neighbours = []
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] != "#":
                        neighbours.append((ni, nj, di, dj))
                    for ddi, ddj in directions:
                        if di == ddi or dj == ddj:
                            continue
                        neighbours.append((i, j, ddi, ddj))
                    adjacency_list[(i, j, di, dj)] = neighbours
    return adjacency_list

def _draw_visited(maze: list[list[str]], visited: set[tuple[int, int, int, int]]) -> str:
    """Draw the visited nodes on the maze."""
    for i, j, _, _ in visited:
        if maze[i][j] not in "SE":
            maze[i][j] = "O"
    return "\n".join("".join(row) for row in maze)


def part1(input):
    """Find the shortest path from S to E.
    
    Moving one space costs 1, rotating 90 degrees costs 1000.
    """
    maze = [list(line) for line in input.splitlines()]
    adjacency_list = _build_adjacency_list(maze)
    start = [((i, j, 0, 1), [(i, j, 0, 1, 0)]) for i, row in enumerate(maze) for j, cell in enumerate(row) if cell == "S"][0]
    heap = []
    heapq.heappush(heap, (0, start))
    cost, visited, on_route = _shortest_path(maze, heap, adjacency_list)
    visited_on_route = {(i, j, dx, dy) for i, j, dx, dy, _ in on_route}
    print(_draw_visited(maze, visited))
    print("")
    print(_draw_visited(maze, visited_on_route))
    return cost


def part2(input):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
