import xlrd

# Достаём файл и распечатываем
tags = []
rb = xlrd.open_workbook(r'2excel.xlsx')
sheet = rb.sheet_by_index(0)
# Создаём матрицу с нулями
way = [[0] * (sheet.nrows - 1) for i in range(sheet.nrows - 1)]
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    if rownum == 0:
        tags = row
    else:
        way[rownum - 1] = row[1:]
# Создаём список адресов
tags = tags[1:]

print('∘ Список учреждений :')
for numb in range(sheet.nrows - 1):
    print('∎',tags[numb])

# Создаём библиотеку для индексации
libr = {}
for i in range(sheet.nrows - 1):
    libr[tags[i]] = i

# Делам inf float-ом и way - списком
inf = float('Inf')
for i in range(sheet.nrows - 1):
    for j in range(sheet.nrows - 1):
        if way[i][j] == 'inf':
            way[i][j] = inf
way = list(way)

# Пользователь вводь место отправления и пункт назначения
value_1 = input('⌂ Место отправления: ')
while value_1 not in tags:
    print('Вы ввели не верный адрес.')
    value_1 = input('⌂ Место отправления: ')
start = libr[value_1]

value_2 = input('⏏ Пункт назначения: ')
while value_2 not in tags:
    print('Вы ввели не верный адрес.')
    value_2 = input('⏏ Пункт назначения: ')
finish = libr[value_2]

# Условие работы
if start == finish:
    print('Вы в пункте назначения. ')
else:
    def dijkstra(way, s):
        n = len(way)

        Q = [(0, s)]

        d = [inf for i in range(n)]
        d[s] = 0
        while len(Q) != 0:
            (cost, u) = Q.pop(0)

            for v in range(n):
                if d[v] > d[u] + way[u][v]:
                    d[v] = d[u] + way[u][v]
                    Q.append((d[v], v))
        return d


    def getPath(finish):
        global d
        distance = 0
        n = len(way)

        path = [finish]
        while finish != start:
            for v in range(n):
                if d[v] == d[finish] - way[finish][v]:
                    distance += way[finish][v]
                    path.append(v)
                    finish = v
        return path[::-1], distance

    d = dijkstra(way, start)

    route, route_length = getPath(finish)

    print('∘ Маршрут: ')
    for i in route:
        if tags[i] != tags[route[-1]]:
            print(tags[i],' ► ',end=' ')
        else:
            print(tags[i],end=' ')

    print(' ')
    print('∘ Длина маршрута: ')
    print(int(route_length),'м' )
