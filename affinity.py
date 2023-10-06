def affinity(use_matrix: list[int], freq_sum: list[int]) -> list[list[int]]:
    attribute_qty = len(use_matrix[0])

    affinity_matrix = [[0 for _ in range(attribute_qty)] for _ in range(attribute_qty)]

    i = 0
    while i < attribute_qty:
        j = 0
        while j <= i:
            component = 0
            for number, query in enumerate(use_matrix):
                if query[i] == 1 and query[j] == 1:
                    component += freq_sum[number]

            affinity_matrix[i][j] = component
            affinity_matrix[j][i] = component

            j += 1

        i += 1

    return affinity_matrix


if __name__ == "__main__":
    for i in affinity(
        [[0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]],
        [[20, 5, 0], [10, 0, 15], [0, 40, 5], [0, 20, 10]],
    ):
        print(i)
