#test matrix
matrix = [
    [1, 1, 1, -1, 0, -1, 0],
    [-1, -1, 1, -1, 1, -1 - 1],
    [0, 1, 1, -1, 1, 1, 1],
    [-1, -1, -1, 1, -1, -1, -1],
    [0, -1, 0, -1, 1, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 0, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 0, -1, 0, -1, 0],
    [1, -1, -1, -1, -1, -1, -1],
    [1, -1, 0, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 0, -1, 0, -1, 0],
    [-1, -1, 1, -1, -1, -1, -1],
    [0, 1, 1, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 0, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 0, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, 1, -1, 0, -1, 0],
    [-1, 1, 1, -1, -1, -1, -1],
    [0, -10, -1, 0, -1, 0],
    [-1, -1, -1, -1, -1, -1, -1],
    [0, -1, -1 - 1, 0, -1, 0]
]
#function to get adjacency
def get_adjacency_matrix(matrix):
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] == 0:
                continue

            d[(i, j)] = []

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

                ni, nj = i + di, j + dj

                if ni < 0 or nj < 0 or ni >= len(matrix) or nj >= len(matrix[ni]):
                    continue

                if matrix[ni][nj] == 0:
                    continue

                d[(i, j)].append((ni, nj))

    return d


def get_islands(matrix):
    am = get_adjacency_matrix(matrix)
#searching land coordinates
    islands = []
    seen = set()
    for coordinate in am:
        if coordinate in seen:
            continue
        island = set()
        position = [coordinate]

        while position:

            current = position.pop(0)
            island.add(current)
            adjacentPosition = am[current]

            for adjacentPoint in adjacentPosition:
                if adjacentPoint not in island:
                    position.append(adjacentPoint)

        islands.append(island)
        seen.update(island)

    return islands

islands = get_islands(matrix)

for island in islands:
    print(island)