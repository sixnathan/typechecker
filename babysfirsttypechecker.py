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


