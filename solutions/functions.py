import math

def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    square = number**2
    return square 


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    return s[::-1]

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """ 
    max_num = lst[0]  
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num 

def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    if n % 2 == 0:
        return "Even" 
    else:
        return "Odd"

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    return s == s[::-1]
def calculate_area(shape, *args):
    """
    This function calculates and returns the area of the specified shape based on the provided arguments.
    The type of shape and its corresponding parameters are passed as arguments.
    
    Supported shapes and their parameters:
    - "circle": radius
    - "rectangle": length, width
    - "triangle": base, height
    
    :param shape: str, the type of the shape for which the area is to be calculated.
    :param args: tuple, the parameters required to calculate the area of the specified shape.
    :return: float, the area of the specified shape.
    
    :raises ValueError: If an unsupported shape is provided or if the number of parameters 
    for the shape is incorrect.
    """
    if shape == "circle":
        radius = args[0]
        area = radius**2 * math.pi 
        return area
    elif shape == "rectangle":
        length = args[0]
        width = args[1]
        area = length * width
        return area
    elif shape == "triangle":
        base = args[0]
        height = args[1]
        area = (base * height)/2
        return area
    else:
        return "not found"
        
        


