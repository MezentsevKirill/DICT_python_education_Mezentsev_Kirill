# Stage 1
def draw_matrix():
    if len(s) == 4:
        print([s[0], s[1]])
        print([s[2], s[3]])
    elif len(s) == 9:
        print([s[0], s[1], s[2]])
        print([s[3], s[4], s[5]])
        print([s[6], s[7], s[8]])
    elif len(s) == 6:
        print([s[0], s[1], s[2]])
        print([s[3], s[4], s[5]])
    elif len(s) == 16:
        print([s[0], s[1], s[2], s[3]])
        print([s[4], s[5], s[6], s[7]])
        print([s[8], s[9], s[10], s[11]])
        print([s[12], s[13], s[14], s[15]])
    elif len(s) == 20:
        print([s[0], s[1], s[2], s[3], s[4]])
        print([s[5], s[6], s[7], s[8], s[9]])
        print([s[10], s[11], s[12], s[13], s[14]])
        print([s[15], s[16], s[17], s[18], s[19]])
    elif len(s) == 25:
        print([s[0], s[1], s[2], s[3], s[4]])
        print([s[5], s[6], s[7], s[8], s[9]])
        print([s[10], s[11], s[12], s[13], s[14]])
        print([s[15], s[16], s[17], s[18], s[19]])
        print([s[20], s[21], s[22], s[23], s[24]])


def draw_matrix_v2():
    if len(s) == 2:
        print(s[0])
        print(s[1])
    elif len(s) == 3:
        print(s[0])
        print(s[1])
        print(s[2])
    elif len(s) == 4:
        print(s[0])
        print(s[1])
        print(s[2])
        print(s[3])
    elif len(s) == 5:
        print(s[0])
        print(s[1])
        print(s[2])
        print(s[3])
        print(s[4])


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
    s = []
    for i in range(n):
        for j in range(m):
            s.append(a[i][j] + b[i][j])
    draw_matrix()
else:
    print("ERROR")
# Stage 2
n, m = map(int, input("Enter the number of lines and columns\n> ").split())
a.clear()
s = []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        continue
const = int(input())
for i in range(n):
    for j in range(m):
        s.append(a[i][j] * const)
draw_matrix()
# Stage 3
calculate_list = [1, 2, 3, 0]
calculate = None
while calculate != calculate_list[3]:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
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
            s = []
            for i in range(n):
                for j in range(m):
                    s.append(a[i][j] + b[i][j])
            draw_matrix()
        else:
            print("ERROR")
    if calculate == calculate_list[1]:
        n, m = map(int, input("Enter the number of lines and columns\n> ").split())
        a.clear()
        s = []
        for i in range(n):
            a.append(list(map(int, input().split())))
            for j in range(m):
                continue
        const = int(input())
        for i in range(n):
            for j in range(m):
                s.append(a[i][j] * const)
        draw_matrix()
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
            draw_matrix_v2()
        else:
            print("The operation cannot be performed")
