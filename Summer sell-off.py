n, f = map(int, input().split())
products = []
clients = []
for i in range(n):
    product, client = map(int, input().split())
    products.append(product)
    clients.append(client)


for i in range(1, len(clients)):
    for j in range(i-1, -1, -1):
        if clients[j] < clients[j+1]:
            clients[j], clients[j+1] = clients[j+1], clients[j]
            products[j], products[j+1] = products[j+1], products[j]
        else:
            break

days = [[x, y] for x, y in zip(products, clients)]
for i in days:
    if i[0] == 0:
        days.remove(i)

sell = 0

for i in range(f):
    days[i][0] = 2*days[i][0]
    sell += min(days[i])

for k in range(f, len(days)):
    sell += min(days[k])

print(sell)
