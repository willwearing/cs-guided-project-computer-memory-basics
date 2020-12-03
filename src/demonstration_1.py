"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
# def to_lower_case(string):
    
"""
Input: string containing lower and uppercase letters
Putput: the lowercased string

The ASCII representation of letters maps letters to number
lowercase letters a-z are mapped to 97-122
uppercase letters A-Z are mapped to 65-90

97-65 = 32
122 - 90 = 32

To take a lowercase letter and capitalize it, we can subtract 32 to its ascii number
To take an uppercase letter and lowercase it, we can add 32 to its ascii number

Strategy:
Look through each letter in the input string
If it's an uppercase letter, add 32 to its ascii value 
If it's already lowercased, then we don't need to do anything 
Return the updated string

How do we check if a letter is upper or lowercased? There are built in's for this, 
but we're not allowed to use them.

Turn every letter in the input into its ascii number 
Iterate through all of the ascii numbers of the input
    Check if see if any of those numbers falls into the range 65-90
    If it does, add 32 to that ascii value
Turn the ascii values back into a string 

"""

#Sean's solution


# #Josh's solution: 
def to_lower_case(string):
    new_string = []
    for letter in string:
      if ord(letter) >= 97:
        new_string.append(letter)
      else:
        new_string.append(chr(ord(letter) + 32))
    return ''.join(new_string)
        
print(to_lower_case("AustenP"))