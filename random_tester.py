

def uniform_test(random_function, *args, N=10000, **kwargs):
    """
    Tests the uniformity of a random function.

    Args:
        random_function (function): The random function to be tested.
        *args: Variable number of arguments to be passed to the random function.
        N (int, optional): The number of times the random function is run. Defaults to 10000.
        **kwargs: Variable number of keyword arguments to be passed to the random function.

    Returns:
        None

    This function tests the uniformity of a given random function by running it N times,
    storing the results, and printing the probabilities and discrepancies.

    The function takes in the random function to be tested, along with any required arguments
    and keyword arguments. It then iterates N times, calling the random function and
    updating the count for each unique random object.

    After running the random function N times, the function prints a header with the
    column names. It then calculates and prints the probability and discrepancy for each
    result. The discrepancy is the absolute difference between the probability and the
    theoretical probability of each result.

    Finally, the function calculates and prints the theoretical probability and the total
    sum of the results.

    Note:
        - This function assumes that the random function returns a unique value each time
          it is called.
        - The return value of random_function needs to be hashable.

    Example:
        >>> uniform_test(random_function, arg1, arg2, N=10000)
        Random Object                   | Probability    | Discrepancy
        -------------------------------------------------------------
        Random Object 1                | Probability     | Discrepancy
        Random Object 2                | Probability     | Discrepancy
        ...
        Theoretical Probability: x.xxxx
        Total Sum: x.xxxx
    """
    results = {}
    
    # Run the random function N times and store the results
    for _ in range(N):
        random_object = random_function(*args,**kwargs)
        
        # Update the count for each unique random object
        if random_object not in results:
            results[random_object] = 1
        else:
            results[random_object] += 1

    # Print header
    print(f"{'Random Object':<30} | {'Probability':<12} | {'Discrepancy':<10}")
    print('-' * 60)

    total_probability = 0
    # Calculate and print the probability and discrepancy for each result
    for k, v in results.items():
        probability = v / N
        total_probability += probability
        discrepancy = round(abs(probability - 1 / len(results)), 4)
        

        k_str = str(k)
        k_lines = k_str.split('\n')  # Split the string into multiple lines

        # Print the first line with the probability
        print(f"{k_lines[0]:<30} | {probability:<12.4f} | {discrepancy:<10.4f}")
        
        # Print any additional lines without the probability column
        for line in k_lines[1:]:
            print(f"{line:<30} | {'':<12}")
        print('-' * 60)

    # Print the total probability
    print(f"Total Probability: {total_probability:.4f}")






def random_test(random_function, *args, N=10000, **kwargs):
    """
    This function tests a given random function by running it N times, storing the results and printing the probabilities.
    
    Parameters:
    random_function (function): The random function to be tested.
    *args: Variable number of arguments to be passed to the random function.
    N (int): The number of times the random function is run. Defaults to 10000.
    **kwargs: Variable number of keyword arguments to be passed to the random function.
    
    Returns:
    None

    Notes:
    - This function assumes that the random function returns a unique value each time it is called.
    - The return value of random_function needs to be hashable.
    """
    results = {}
    total_probability = 0
    
    # Run the random function N times and store the results
    for _ in range(N):
        random_object = random_function(*args, **kwargs)
        
        # Update the count for each unique random object
        results[random_object] = results.get(random_object, 0) + 1

    # Print header
    print(f"{'Random Object':<30} | {'Probability':<12}")
    print('-' * 60)

    # Calculate and print the probability for each result
    for k, v in results.items():
        probability = v / N
        total_probability += probability
        k_str = str(k)
        k_lines = k_str.split('\n')  # Split the string into multiple lines

        # Print the first line with the probability
        print(f"{k_lines[0]:<30} | {probability:<12.4f}")
        
        # Print any additional lines without the probability column
        for line in k_lines[1:]:
            print(f"{line:<30} | {'':<12}")
        
        print('-' * 60)

        # Print the total probability
    print(f"Total Probability: {total_probability:.4f}")

