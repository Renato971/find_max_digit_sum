# find_max_digit_sum

The task is to find the string with the highest sum of digits from a list of alphanumeric strings. 

Each digit in a string is treated separately, meaning that for a string like "36", the digits are summed as 3 + 6. The program processes the list by examining each string, identifying the digits it contains, and calculating their total. While iterating, it keeps track of the largest sum encountered. After all strings have been evaluated, it returns the maximum digit sum. 

This approach is simple because it uses basic loops and conditional statements. It assumes that the list contains no more than ten strings, each with a maximum length of twelve characters, and treats strings without digits as having a sum of zero. 

The code is saved in a file named find_max_digit_sum.py and executed using Python. Test cases such as ["abc", "xyz"] returning 0, ["a1", "b2", "c3"] returning 3, and ["h1n36", "z99"] returning 18, help verify its correctnes.
