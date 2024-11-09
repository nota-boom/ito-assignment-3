def northwest_corner_method(coefficients, supply, demand):
    if sum(supply) != sum(demand):
        print("Method is not applicable!")
        return []
    n = len(supply)
    m = len(demand)
    result = [[0] * m for _ in range(n)]
    row, col = 0, 0

    while row < n and col < m:
        num = min(supply[row], demand[col])
        result[row][col] = num
        supply[row] -= num
        demand[col] -= num

        if supply[row] == 0:
            row += 1
        if demand[col] == 0:
            col += 1
    res = 0
    for i in range(n):
        for j in range(m):
            if result[i][j] != 0:
                res += result[i][j] * coefficients[i][j]
    print(f"Solution = {res}")
    return result


def vogel(coefficients, supply, demand):
    if sum(supply) != sum(demand):
        print("Method is not applicable!")
        return []
    INF = 10 ** 6
    n = len(supply)
    m = len(demand)
    res = 0
    x_0 = []

    while max(supply) != 0 or max(demand) != 0:
        row = []
        for i in range(n):
            arr = sorted(coefficients[i][:])
            if len(arr) > 1:
                row.append(arr[1] - arr[0])
            else:
                row.append(0)
        col = []
        for j in range(m):
            arr = []
            for i in range(n):
                arr.append(coefficients[i][j])
            arr = sorted(arr)
            if len(arr) > 1:
                col.append(arr[1] - arr[0])
            else:
                col.append(0)

        row_max = max(row)
        col_max = max(col)

        if (row_max >= col_max):
            for ind, val in enumerate(row):
                if (val == row_max):
                    min_row = min(coefficients[ind])
                    for ind2, val2 in enumerate(coefficients[ind]):
                        if (val2 == min_row):
                            min_col = min(supply[ind], demand[ind2])
                            res += min_col * min_row
                            supply[ind] -= min_col
                            demand[ind2] -= min_col
                            x_0.append((ind, ind2, min_col))

                            if (demand[ind2] == 0):
                                for r in range(n):
                                    coefficients[r][ind2] = INF
                            else:
                                coefficients[ind] = [INF for _ in range(m)]
                            break
                    break
        else:
            for ind, val in enumerate(col):
                if (val == col_max):
                    min_row = INF
                    for j in range(n):
                        min_row = min(min_row, coefficients[j][ind])

                    for ind2 in range(n):
                        val2 = coefficients[ind2][ind]
                        if val2 == min_row:
                            min_col = min(supply[ind2], demand[ind])
                            res += min_col * min_row
                            supply[ind2] -= min_col
                            demand[ind] -= min_col
                            x_0.append((ind2, ind, min_col))

                            if (demand[ind] == 0):
                                for r in range(n):
                                    coefficients[r][ind] = INF
                            else:
                                coefficients[ind2] = [INF for _ in range(m)]
                            break
                    break

    sol = [[0] * m for _ in range(n)]
    for i, j, x_ij in x_0:
        sol[i][j] = x_ij
    print(f"Solution = {res}")
    return sol


def russel(coefficients, supply, demand):
    if sum(supply) != sum(demand):
        print("Method is not applicable!")
        return []
    n = len(supply)
    m = len(demand)
    INF = -10 ** 6
    res = [[0] * m for _ in range(n)]
    res_sum = 0
    while max(supply) != 0 or max(demand) != 0:
        cols = []
        rows = []
        temp = [[0] * m for _ in range(n)]


        for row in coefficients:
            rows.append(max(row))
        for j in range(m):
            max_col = coefficients[0][j]
            for i in range(1, n):
                if coefficients[i][j] > max_col:
                    max_col = coefficients[i][j]
            cols.append(max_col)
        for i in range(n):
            for j in range(m):
                if coefficients[i][j] != INF:
                    temp[i][j] = coefficients[i][j] - cols[j] - rows[i]

        min_value = float('inf')
        min_index = (INF, INF)
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j] < min_value:
                    min_value = temp[i][j]
                    min_index = (i, j)
        i, j = min_index
        num = min(supply[i], demand[j])
        res[i][j] = num
        res_sum += num * coefficients[i][j]
        supply[i] -= num
        demand[j] -= num

        if supply[i] == 0:
            for k in range(m):
                coefficients[i][k] = INF
        if demand[j] == 0:
            for k in range(n):
                coefficients[k][j] = INF
    print(f"Solution = {res_sum}")
    return res


print("North-West algorithm")
coefficients = [[7, 1, 13, 10], [1, 10, 200, 1], [8, 9, 4, 5]]
supply = [6, 7, 18]
demand = [6, 7, 8, 10]
for row in northwest_corner_method(coefficients, supply, demand):
    print(row)

print("\nVogel's approximation")
coefficients = [[7, 1, 13, 10], [1, 10, 200, 1], [8, 9, 4, 5]]
supply = [6, 7, 18]
demand = [6, 7, 8, 10]
for row in vogel(coefficients, supply, demand):
    print(row)

print("\nRussel's approximation")
coefficients = [[7, 1, 13, 10], [1, 10, 200, 1], [8, 9, 4, 5]]
supply = [6, 7, 18]
demand = [6, 7, 8, 10]
for row in russel(coefficients, supply, demand):
    print(row)
