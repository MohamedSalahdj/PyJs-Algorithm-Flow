import sys

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Define the graph as an adjacency matrix
data = [[0, 2, 4, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 7, 4, 6, 0, 0, 0],
        [0, 0, 0, 0, 3, 2, 4, 0, 0, 0], [0, 0, 0, 0, 4, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4, 0], [0, 0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


n = len(data)

# Initialize states array to store the best known cost to reach each node
states = [None] * n
states[n-1] = {"from": '', "to": '', "cost": 0}

for i in range(n-2, -1, -1):
    states[i]= {"from": labels[i], "to": '', "cost": sys.maxsize}
    for j in range(i-1, n):
        if data[i][j] == 0:
            continue
        new_cost = data[i][j] + states[j]['cost']
        if new_cost < states[i]['cost']:
            states[i]['cost'] = new_cost
            states[i]['to'] = labels[j]
        
print(f"Minimum cost from {labels[0]} to {labels[n-1]}:", states[0]['cost'])


# Compute the minimum cost and path from A to J using the computed states
path = [labels[0]]
j = 0

for i in range(0, n):
    if states[i]['from'] == path[j]:
        path.append(states[i]['to'])
        j +=1

print("Path:", end=" ")
print(' -> '.join(path))

