def foobar(name : str | None) -> str: 
    return "Fizz"

buzz : int = 42 

# a type checker would go through the code above and ensure that it follows the specs in the annotations above 
# it would enforce that name is of types string and that the function always returns something of type string  

# we want to be able to enforce typechecking to prevent errors like the following: 

from __future__ import annotations 

def greet(name : str | None) -> str: 
    if name is None: 
        return 42 
    return "Hello, " + name 

# this has two possible types that it could return: a string or an int, but in the annotations it specifies that it should be of type string  

age : int = '42' 
# similarly this specifies that the type of age should be an int, yet we assign to it a string. 

def length(xs: list[int]) -> int: 
    return len(xs) + xs 

# this attempts to add together a list of ints and an int, and return an int. the opeartion + is not defined between int and list of int



