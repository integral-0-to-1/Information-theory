from math import log2
from prettytable import PrettyTable

n = 20
m = n ** 2
volume_of_information = 0
matr1 = [[0 for i in range(n)] for j in range(n)]


def draw(obj: list, first_row: list, first_col=None):
    x = PrettyTable()
    x.field_names = first_row
    for index, val in enumerate(obj):
        if first_col is not None:
            val.insert(0, first_col[index])
        else:
            val.insert(0, index+1)
        x.add_row(val)
    print(x)



for i in range(len(matr1)):
    for j in range(len(matr1[i])):
        matr1[i][j] = int(2 * (j + 1 - 2.5) + 3 * (i + 1))


maxY = matr1[0][0]
for i in range(len(matr1)):
    for j in range(len(matr1[i])):
        if matr1[i][j] > maxY:
            maxY = matr1[i][j] + 1


matr2 = [[0 for i in range(maxY)] for j in range(2)]
matr3 = [[0 for i in range(maxY)] for j in range(n)]
matr4 = [[0 for i in range(maxY)] for j in range(n)]


for i in range(maxY):
    for j in matr1:
        matr2[1][i] += j.count(i)
    matr2[0][i] = matr2[1][i]/m


for i in range(len(matr3)):
    for j in range(len(matr3[i])):
        if 1 <= (j - 2 * (i + 1 - 2.5))/3 <= n and (int((j - 2 * (i + 1 - 2.5)) / 3) - (j - 2 * (i + 1 - 2.5)) / 3) == 0:
            matr3[i][j] = 1 / m


for i in range(len(matr4)):
    for j in range(len(matr4[i])):
        if 1 <= (j - 2 * (i + 1 - 2.5))/3 <= n and (int((j - 2 * (i + 1 - 2.5)) / 3) - (j - 2 * (i + 1 - 2.5)) / 3) == 0:
            matr4[i][j] = log2(1/matr2[1][j] * n) / m
            volume_of_information += matr4[i][j]


print("\033[7m\033[36m Таблиця 1 \033[0m")
draw(matr1, ["X1/X2"] + [str(i+1) for i in range(n)])


print("\n\n\033[7m\033[36m Таблиця 2 \033[0m")
draw(matr2, ["Y"] + [str(i) for i in range(maxY)], ["Pij", "n"])


print("\n\n\033[7m\033[36m Таблиця 3 \033[0m")
draw(matr3, ["Y/X1"] + [str(i) for i in range(maxY)])


print("\n\n\033[7m\033[36m Таблиця 4 \033[0m")
draw(matr4, ["Y/X1"] + [str(i) for i in range(maxY)])


print(f"\n\n\033[7m\033[1m\033[36m Загальний обсяг інформації = {volume_of_information} \033[0m")
