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
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0],
    ]
    freq_matrix = [
        [20, 5, 0],
        [10, 0, 15],
        [0, 40, 5],
        [0, 20, 10],
    ]
    sum_vec = freq_sum(freq_matrix, [1, 1, 1])
    print("sum vec =", sum_vec)

    aff = affinity(use_matrix, sum_vec)
    for i in aff:
        print(i)
    print("#########################")
    ca_matrix = ca(aff, [0, 1, 2, 3])
    print("#########################")
    print("Order= ", ca_matrix[1])
    for i in ca_matrix[0]:
        print(i)

    print(fragment(use_matrix, freq_matrix, ca_matrix[0], ca_matrix[1], sum_vec))


if __name__ == "__main__":
    main()
