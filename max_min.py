def max_min(list):
    if not list:
        return None, None
    
    max_val = max(list)
    min_val = min(list)

    return max_val, min_val

my_list = [1, 3, 6, 9, 12]
max_element, min_element = max_min(my_list)
print("Maximum element:", max_element)
print("Minimum element:", min_element)