items = [
    {
      "name": "#1",
      "weight": 1,
      "profit": 4
    }, {
      "name": "#2",
      "weight": 3,
      "profit": 9
    }, {
      "name": "#3",
      "weight": 5,
      "profit": 12
    }, {
      "name": "#4",
      "weight": 4,
      "profit": 11
    }
]


max_weight = 8

items.insert(0, {"name": "#0", "weight": 0, "profit": 0})

# Initialize the DP table
dp = [ [0 for _ in range(max_weight + 1)] for _ in range(len(items))]


# Fill in the dp array using dynamic programming
for i in range(1, len(items)):
    for w in range(1, max_weight + 1):
        if items[i]["weight"] <= w:
            dp[i][w] = max(items[i]["profit"] + dp[i - 1][w - items[i]["weight"]],
                           dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]


print(f"DP Table: {dp}")
print("-" * 45)
print("Max Profit:", dp[-1][-1]) 

# Backtrack to find the items included in the optimal solution

solution = []
remaining_weight = max_weight
i = len(items) - 1
j = max_weight

while remaining_weight >= 0 and j > 0:
    if dp[i][j] > dp[i-1][j]:
        solution.append(items[i]["name"])
        remaining_weight -= items[i]["weight"]
        i -= 1
        j = remaining_weight 
    else:
         i -= 1

print("-" * 45)
print("Items included in the optimal solution:", solution)