n, b = input().split()
n, b = int(n), int(b)
rotas = []
consultas = []

for _ in range(b):
    i, j, p = input().split()
    i, j, p = int(i), int(j), int(p)
    # rotas[f'{i,j}'] = (p)
    rotas.append((i, j, p))

print(rotas)

c = int(input())

for _ in range(c):
    e, d = input().split()
    e, d = int(e), int(d)
    consultas.append((e, d))

for consulta in consultas:
    max_passag = 0
    embarque = consulta[0]
    destino = consulta[1]
    
    possibs = [op for op in rotas if op[0] == embarque]
    print(possibs)

