class knapsack:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.total_value = 0
        self.items = []
    
    def add_item(self, new_item):
        if new_item.weight > self.max_capacity - self.current_capacity:
            available_capacity = self.max_capacity - self.current_capacity
            new_item.weight = available_capacity
            new_item.value = available_capacity * new_item.ratio
        
        self.items.append(new_item)
        self.current_capacity += new_item.weight 
        self.total_value += new_item.value 


class Item:
    def __init__(self, value, weight, name):
        self.value = value
        self.weight = weight
        self.name = name
        self.ratio = value / weight if weight != 0 else 0
    
    def __repr__(self):
        return f'[{self.name} , value: {self.value} , weight: {self.weight} , ratio: {self.ratio}]'