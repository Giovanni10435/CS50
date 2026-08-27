def Solution(cost):
    cost.sort(reverse=True)

    total = 0

    for i in range(len(cost)):
        if (i + 1) % 3 != 0:
            total += cost[i]

    return total


candies = int(input("Insira quantos doces quer comprar: "))
costs = [0] * candies

for candy in range(candies):
    costs[candy] = int(input("Insira o custo de cada doce: "))

print("Custos dos doces:", costs)

print("Custo mínimo:", Solution(costs))