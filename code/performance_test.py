"""
This short script helps you to evaluate the performance of your written functions.
It calls the functions k times and measures the time they needed.
"""

import time

# Import the solution
import p0053_Combinatoric_selections_TODO as sol

"""
Assigning the function variables of the functions in the solution.
Inserting them with the arguments as 'index : (function, arguments)'
Note that the arguments need to be packed in a tuple.
"""
args = ()
functions = {0: (sol.sol, args),
             1: (sol.sol2, args)
             }

"""
Adjust the number of calls. Try some different values, depending on the problem.
If it is very easy, you may need more calls to get comparable values.
"""
k = 150

# Go through the dict
for key in functions:

    # Get the function and its arguments
    func, args = functions[key]

    # Save current time
    start_time = time.time()

    # Call the function k times
    for _ in range(k):
        func(*args)

    # Compute the time the function needed and print all informations
    t = time.time() - start_time
    print(f"{t:.7f} secs for '{func.__name__}' ")


