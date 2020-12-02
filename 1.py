l = []
with open('input.txt') as f:
    l = f.read().splitlines()
for i in range(len(l)-1, -1, -1):
    if l[i] == ' ' :
        if l[i - 1] == ' ':
            l[i] = ''
print(l)
