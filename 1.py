f = open('input.txt')                                  
print(f.read())
result = []
for line in f:
   line = line.split()
   result.append(line)
print(" ".join(map(str, result)))






f1 = 'input.txt'
result = []
with open(f1) as file:
    print(file.read())
    for line in f1:
        line = line.split()
        result.append(line)
print(" ".join(map(str, result)))
