from affinity import affinity


def bond(A: list[int], B: list[int]) -> int:
    total = 0

    for i in range(0, len(A)):
        total += A[i]*B[i]

    return total


def cont(A: list[int], B: list[int], C: list[int]) -> int:
    return 2*bond(A, B) + 2*bond(B, C) - 2*bond(A, C)


def ca(affinity_matrix: list[list[int]], atributes: list[int]) -> (list[list[int]], list[str]):

    atributes_len = len(atributes)
    atribute_zero = [0 for _ in range(atributes_len)]

    ca_matrix = list()
    ca_atributes = list()

    ca_atributes.append(atributes.pop(0))
    ca_matrix.append(affinity_matrix.pop(0))

    for atribute_vals in affinity_matrix:
        cont_values = [float('-inf') for _ in range(atributes_len)]

        cont_values[0] = cont(atribute_zero, atribute_vals, ca_matrix[0])

        for index in range(1, len(ca_matrix)-1):
            cont_values[index] = cont(
                ca_matrix[index-1], atribute_vals, ca_matrix[index])

        cont_values[len(ca_matrix)] = cont(
            ca_matrix[len(ca_matrix)-1], atribute_vals, atribute_zero)

        ca_atributes.insert(cont_values.index(
            max(cont_values)), atributes.pop(0))

        ca_matrix.insert(cont_values.index(
            max(cont_values)), atribute_vals)
        print(ca_atributes)

    return (ca_matrix, ca_atributes)


if __name__ == "__main__":
    aff = [[45, 0, 45, 0], [0, 80, 5, 75], [45, 5, 53, 3], [0, 75, 3, 78]]
    print(aff)
    print(ca(aff, [1, 2, 3, 4]))
