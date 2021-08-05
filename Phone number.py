"""Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number."""


def create_phone_number(n):
    a="".join(map(str, n[0:3]))
    b="".join(map(str, n[3:6]))
    c="".join(map(str, n[6:]))
    return f"({a}) {b}-{c}"

print(create_phone_number([1,2,3,4,5,6,7,8,9]))