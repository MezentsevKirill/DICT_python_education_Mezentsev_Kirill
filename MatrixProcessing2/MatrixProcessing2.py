# Stage 1
a = []
b = []
s = []
# Stage 1,2,3,4,5,6
calculate_list = [1, 2, 3, 0, 4, 5, 6]
calculate = None
while calculate != calculate_list[3]:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n"
          "5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    calculate = int(input("Your choice: > "))
    if calculate == calculate_list[0]:
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        a = []
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        b = []
        for i in range(n):
            b.append(list(map(int, input().split())))
            for j in range(m):
                continue
        a_unpacked = [j for i in a for j in i]
        b_unpacked = [j for i in b for j in i]
        if len(a_unpacked) == len(b_unpacked):
            length = len(a)
            length1 = len(b)
            s = [[0 for j in range(length1)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    s[i][j] = a[i][j] + b[i][j]
            for elem in s:
                print(elem)
        else:
            print("ERROR")
    if calculate == calculate_list[1]:
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        a.clear()
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        const = int(input())
        length = len(a)
        s = [[0 for j in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                s[i][j] = (a[i][j] * const)
        for elem in s:
            print(elem)
    if calculate == calculate_list[2]:
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        a.clear()
        b.clear()
        s.clear()
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        p, f = map(int, input("Enter the number of lines and columns\n> ").split())
        for i in range(p):
            b.append(list(map(int, input().split())))
            for j in range(f):
                continue
        if m == p:
            length = len(a)
            length1 = len(b)
            s = [[0 for j in range(length1)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        s[i][j] += a[i][k] * b[k][j]
            for elem in s:
                print(elem)
        else:
            print("The operation cannot be performed")
    if calculate == calculate_list[4]:
        transposition_list = [1, 2, 3, 4]
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        transposition = int(input("Your choice: > "))
        a.clear()
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        if transposition == transposition_list[0]:
            if len(a) == 2:
                print([a[0][0], a[1][0]])
                print([a[0][1], a[1][1]])
            if len(a) == 3:
                print([a[0][0], a[1][0], a[2][0]])
                print([a[0][1], a[1][1], a[2][1]])
                print([a[0][2], a[1][2], a[2][2]])
        if transposition == transposition_list[1]:
            if len(a) == 2:
                print([a[1][1], a[0][1]])
                print([a[1][0], a[0][0]])
            if len(a) == 3:
                print([a[2][2], a[1][2], a[0][2]])
                print([a[2][1], a[1][1], a[0][1]])
                print([a[2][0], a[1][0], a[0][0]])
        if transposition == transposition_list[2]:
            if len(a) == 2:
                print([a[0][1], a[0][0]])
                print([a[1][1], a[1][0]])
            if len(a) == 3:
                print([a[0][2], a[0][1], a[0][0]])
                print([a[1][2], a[1][1], a[1][0]])
                print([a[2][2], a[2][1], a[2][0]])
        if transposition == transposition_list[3]:
            if len(a) == 2:
                print([a[1][0], a[1][1]])
                print([a[0][0], a[0][1]])
            if len(a) == 3:
                print([a[2][0], a[2][1], a[2][2]])
                print([a[1][0], a[1][1], a[1][2]])
                print([a[0][0], a[0][1], a[0][2]])
    if calculate == calculate_list[5]:
        a.clear()
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        if len(a) == 2:
            det = a[0][0] * a[1][1] - a[1][0] * a[0][1]
            print("The result is:\n", det)
        if len(a) == 3:
            det = a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2]) - a[0][1] * (a[1][0] * a[2][2] - a[2][0] * a[1][2])\
                  + a[0][2] * (a[1][0] * a[2][1] - a[2][0] * a[1][1])
            print("The result is:\n", det)
    if calculate == calculate_list[6]:
        a.clear()
        new_a = []
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        if len(a) == 2:
            det = a[0][0] * a[1][1] - a[1][0] * a[0][1]
            if det != 0:
                t = [a[0][0], a[1][0], a[0][1], a[1][1]]
                e = [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]
                for i in range(2):
                    for j in range(2):
                        new_a.append((1 / det) * e[i][j])
                print("The result is:\n", "%.2f" % new_a[0], "%.2f" % new_a[1], "\n", "%.2f" % new_a[2],
                      "%.2f" % new_a[3])
        if len(a) == 3:
            det = a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2]) - a[0][1] * (a[1][0] * a[2][2] - a[2][0] * a[1][2])\
                  + a[0][2] * (a[1][0] * a[2][1] - a[2][0] * a[1][1])
            if det != 0:
                t = [a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1], a[0][2], a[1][2], a[2][2]]
                e = [[a[1][1] * a[2][2] - a[1][2] * a[2][1], -(a[0][1] * a[2][2] - a[0][2] * a[2][1])
                     , a[0][1] * a[1][2] - a[0][2] * a[1][1]], [-(a[1][0] * a[2][2] - a[1][2] * a[2][0])
                     , a[0][0] * a[2][2] - a[0][2] * a[2][1], -(a[0][0] * a[1][2] - a[0][2] * a[1][0])]
                     , [a[1][0] * a[2][1] - a[1][1] * a[2][0], -(a[0][0] * a[2][1] - a[0][1] * a[2][0])
                     , a[0][0] * a[1][1] - a[0][1] * a[1][0]]]
                for i in range(3):
                    for j in range(3):
                        new_a.append((1 / det) * e[i][j])
                print("The result is:\n", "%.2f" % new_a[0], "%.2f" % new_a[1], "%.2f" % new_a[2], "\n",
                      "%.2f" % new_a[3], "%.2f" % new_a[4], "%.2f" % new_a[5], "\n",
                      "%.2f" % new_a[6], "%.2f" % new_a[7], "%.2f" % new_a[8])
