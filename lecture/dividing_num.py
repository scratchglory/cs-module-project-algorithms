# Artem's 07.13.20
# We'll say that a positive int divides itself if every digit in the number divides into the number evenly.
# So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself.
# Write a function to determine if a number divides itself.

def divides_self(num):
    # make an original copy of Num
    # Loop over each digit in num:
    # get the rightmost digit of NUM using num % 10
    # take that digit, and get remainded of num / digit
    # if remainded is NOT 0, return False
    # take that digit, and get remainder of original num / digit
    # if remainded is NOT 0, return False
    # remove the last digit from the number using // 10 (integer division)

    # return True

    pass


print(divides_self(128))  # true
print(divides_self(12))  # true
print(divides_self(120))  # false

# NOTES:
''' 
UPER
1. Inputs:
    - a number
    - positive integer
    - how may?
    - O - case? return false
    - valid?

2. Outputs?
    - Boolean

3. Plan:
    - Pseudocode
    - how to get a digit?
'''
