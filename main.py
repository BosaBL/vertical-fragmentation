from affinity import affinity
from ca_matrix import ca
from fragments import fragment


def freq_sum(freq_matrix: list[list[int]], freq_vector: list[int]):
    freq_sum = list()

    for row in freq_matrix:
        sum = 0
        for idx in range(len(freq_vector)):
            sum += row[idx] * freq_vector[idx]
        freq_sum.append(sum)

    return freq_sum


def main():
    use_matrix = [
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    ]
    freq_matrix = [
        [15, 20, 10],
        [5, 0, 0],
        [25, 25, 25],
        [3, 0, 0],
        [25, 0, 25],
        [5, 0, 10],
        [1, 20, 10],
        [5, 90, 10],
    ]
    sum_vec = freq_sum(freq_matrix, [1, 1, 1])

    print("##########################")
    print("Matriz de Afinidad")
    aff = affinity(use_matrix, sum_vec)
    for i in aff:
        print(i)
    print("#########################")
    ca_matrix = ca(aff, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("#########################")
    print("Order = ", ca_matrix[1])
    print("Matriz CA")
    for i in ca_matrix[0]:
        print(i)
    print("#########################")

    print("FRAGMENTOS")

    print(
        list(
            map(
                lambda x: [i + 1 for i in x],
                fragment(
                    use_matrix,
                    freq_matrix,
                    ca_matrix[0],
                    ca_matrix[1],
                    sum_vec,
                ),
            )
        )
    )


if __name__ == "__main__":
    main()
