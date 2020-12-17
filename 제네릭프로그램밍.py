from typeing import TypeVar

A = TypeVar('T')
B = TypeVar('U')

def are_equal(a: T, b: U) -> bool :
    return a == b

are_equal(10, 10.0)