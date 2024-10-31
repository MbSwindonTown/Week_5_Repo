def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """
    total = []
    

    for i in range(min_value,max_value + 1):
        if min_value > 0 and max_value > 0:
            if type(min_value) == int and type(max_value) == int:
                if i % 2 ==0: 
                    total.append(i)
                            
        else:
            print("Invalid number")
            break
    print(sum(total))


    # Function implementation here ...
    
    
    return total

# # # Run code example
# min_value = 10
# max_value = 13
# result = sum_of_evens(min_value, max_value) # returns 22
sum_of_evens(12,21)