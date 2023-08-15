n = int(input())
queue = []
biggest = 0

for _ in range(n):
    i = int(input())
    if i in queue:
        while True:
            dequeued = queue.pop(0)
            if len(queue) == 0 or dequeued == i:
                break

    queue.append(i)
    if biggest < len(queue):
        biggest = len(queue)

print(biggest)
