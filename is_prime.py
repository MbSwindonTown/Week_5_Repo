def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    output =  False
    
    if num == 0 or num == 1:
        print(output)
    elif num > 1:
            for i in range(2,num):
                 if (i % 1) == 0:
                      output = True
                      break

    print(output)



    return output


# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
is_prime(10)