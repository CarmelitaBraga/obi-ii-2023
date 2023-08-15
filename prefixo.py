def compara (p1, p2, len1, len2):
    i = 0
    i_max = len1 if len1 <= len2 else len2
    while True:
        if i == i_max or p1[i] != p2[i]:
            print(i)
            break
        i += 1

len1 = int(input())
p1 = input()
len2 = int(input())
p2 = input()
compara(p1, p2, len1, len2)