# self study at home


list_item = [1, 2, 3, 4, 5, 6, ]

def max_value(arg):
    current_max = arg[0]
    for i in arg[1:]:
        if current_max < i:
            current_max = i
    return current_max
        
print(max_value(list_item))