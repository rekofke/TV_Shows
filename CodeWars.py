# 1. Solution - Even or Odd 
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'

# 2. Solution - Convert a Number to a String
# We need a function that can transform a number (integer) into a string.

def number_to_string(num):
    return f"{num}"

# 3. Solution - Remove String Spaces
# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
      return x.replace(" ", "")

# 4. Vowel count
"""Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""

def get_cont(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for c in sentence if c in vowels)