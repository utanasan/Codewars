"""An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case."""


def is_isogram(string):
    l_string=string.lower()
    for i in l_string:
        if l_string.count(i)>1:
            return False
    return True

print(is_isogram("moOse"))
print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba" ))