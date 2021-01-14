"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

'Unsigned' means the integer can only represent positive numbers

String representations of numbers
Integer representations of numbers
Binary representations of numbers

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""
def hamming_weight(n):
    """
    Input: unsigned integer
    Output: integer representing the number of 1's in the binary representation of 'n'

    How can we turn an integer into its binary representation?
    Use bin() function to get a binary representation of 'n'
    The output of bin() will always start with '0b'
    We could remove the leading 0b, but it doesn't affect the number of 1's 
    in the binary representation, so there's no need

    If we already have a binary representation in string format, then we can iterate
    over it and count the numbers of 1's

    """

    # bin_rep = bin(n)
    # counter = 0
    # for digit in bin_rep:
    #     if digit == '1':
    #         counter += 1
    # return counter

    return bin(n).count('1')

print(hamming_weight(4294967291))
print(hamming_weight(201))

"""
You can turn a binary string back into an int using the int() function 
Don't forget to pass int() the arg indicating that the input is a binary string:
int('11111111111111111111111111111011', 2) #4294967291
"""