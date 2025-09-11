def print_array(items):
    print("Name\t Value\t Weight\tratio")
    for item in items:
        print(f" {item.name}\t {item.value}\t {item.weight}\t {item.ratio}")

def print_items(bag):
    print('-'*45)
    print(f"Total Value: {bag.total_value}")
    print(f"Current Capacity: {bag.current_capacity}")
    print("items:")
    print("Name\t Value\t Weight")
    for item in bag.items:
        print(f" {item.name}\t {item.value}\t {item.weight}")