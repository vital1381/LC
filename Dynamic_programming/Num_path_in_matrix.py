import numpy as np


# max number of paths from 0,0 to n,m in matrix of 1 and 0
def max_num_path_in_matrix(a):
    table = np.array(a)
    t = table.shape
    table = np.zeros(t)

    n = 0
    m = 0

    if len(t) == 2:
        n, m = t

        for i in range(0, n):
            table[i][0] = 1
        for j in range(0, m):
            table[0][j] = 1

    if len(t) == 1:
        n = t
        for i in range(0, n):
            table[i] = 1



    # 3 traversal row then col if row or col > boundaries then 0
    for row in range(1, n):
        for col in range(1, m):
            if a[row][col] != 1:
                table[row][col] = 0
            else:
                res = table[row - 1][col] + table[row][col - 1] % (1e9 + 7)
                table[row][col] = res
    res = int(table[n - 1][m - 1])
    return res


if __name__ == "__main__":
    a = [[1, 1, 1], [0, 1, 1]]
    a1 = [[1,1]]
    print (np.array(a1).shape)
    #print(max_num_path_in_matrix(a))
