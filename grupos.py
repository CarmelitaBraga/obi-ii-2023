e, m, d = input().split()
e = int(e)
m = int(m)
d = int(d)
rest = 0
loves = 0
love = []

for _ in range(m):
    line = input().split()
    if int(line[0]) > int(line[1]):
        line[0], line[1] = line[1], line[0]
    love.append((line[0], line[1]))

restric = []
for _ in range(d):
    line = input().split()
    if int(line[0]) > int(line[1]):
        line[0], line[1] = line[1], line[0]
    restric.append((line[0], line[1]))

n_grupos = int(e/3)
for _ in range(n_grupos):
    grupos = []
    line = input().split()
    grupos.append(line)

    for tuple in restric:
        if tuple[0] in line and tuple[1] in line:
            rest += 1
            break
    
    for tuple in love:
        if tuple[0] in line and tuple[1] in line:
            loves += 1
            break

print(rest + (m - loves))



