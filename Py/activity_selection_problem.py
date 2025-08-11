def greedy_activity_selector(start, end):
    result = [0]
    j = 0
    
    for i in range(1, len(start)):
        if start[i] >= end[j]:
            result.append(i)
            j = i
    
    return result

def main():
    start = [9, 10, 11, 12, 13, 14]
    end = [11, 11, 12, 14, 15, 16]  
    
    return greedy_activity_selector(start, end)

print(main())