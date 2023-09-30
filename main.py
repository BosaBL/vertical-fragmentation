from affinity import *
from ca_matrix import *
from fragments import *

def main():
    use_matrix = [[0,1,1,0,1],[1,1,1,0,1],[1,0,0,1,1],[0,0,1,0,0],[1,1,1,0,0]]
    freq_matrix = [[20,5,0],[10,0,15],[0,40,5],[0,20,10],[0,15,0]]

    aff = affinity(use_matrix, freq_matrix)

    ca_matrix = ca(aff,[0,1,2,3,4])

    print(fragment(use_matrix, freq_matrix, ca_matrix[0], ca_matrix[1]))

if __name__ == "__main__":
    main()
