from sort import merge_sort
from knapsack import knapsack, Item
from printing_output import print_array, print_items


# create arrays of randomly assigned values and weights
values = [4, 9, 12, 11, 6, 5]
weights = [1, 2, 10, 4, 3, 5]

# create array of items
items = []
for i in range(len(values)):
    new_item = Item(values[i], weights[i], f'#{i}')
    items.append(new_item)


# Sorting the array of Item objects based on the ratio of value to weight
merge_sort(items, 0, len(items) - 1)

print_array(items)

bag = knapsack(12)

i = 0
while bag.current_capacity < bag.max_capacity:
    bag.add_item(items[i])
    i +=1

print_items(bag)