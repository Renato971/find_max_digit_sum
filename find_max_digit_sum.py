"""
Find your max digit sum from the array
----------------------------------------------
This will take an array of alphanumeric strings and finds the largest sum of digits
in any string from the array

Example:
Input:  ["gt6gu3as", "dq7klwb9x", "as7gg3cmn", "d1d2fh"]
Output: 16
"""

def max_dig_sum(strings):
    """Function to find the largest sum of digits in a list of strings

    Parameters:
        strings (list): A list of strings containing letters and digits.

    Returns:
        int: The largest sum of digits found in the below string"""
    maxSum = 0  # This will hold the largest digit of sum that is found

    # Will go through on each string in the array list
    for s in strings:
        currentSum = 0  # Stores the sum of digits for this string

        # Goes through each character in the string
        for ch in s:
            # Checks if the character is a digit
            if ch.isdigit():
                # Converts the digit character to an integer and add it to the sum
                currentSum += int(ch)

        # After summing the digits in each string, checks if it is the largest found
        if currentSum > maxSum:
            maxSum = currentSum

    return maxSum


# Example:
if __name__ == "__main__":
    array = ["gt6gu3as", "dq7klwb9x", "as7gg3cmn", "d1d2fh"]
    result = max_dig_sum(array)
    print("The largest sum of digits is:", result)  # Expected output: 16
