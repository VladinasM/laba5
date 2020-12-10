# Загрузка файла
with open('input.txt', 'r') as txt_in:
    txt_do = (txt_in.read())
print(txt_do)

# Преобразование в список
wrd_list = txt_do.split(' ')
print(wrd_list)

# Избавление от пробелов
while ('') in wrd_list:
    wrd_list.remove('')

final_version = ''

# Создание конечного варианта
for word in range(len(wrd_list)):
    final_version +=(str(' '+wrd_list[word]))
print(' '+final_version)

# Выгрузка нового файла
with open('output.txt', 'wt') as txt_out:
    txt_out.write(final_version)
