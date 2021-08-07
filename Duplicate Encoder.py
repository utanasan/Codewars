#The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    new_string=""
    for i in word.lower():
        if word.lower().count(i)>1:
            new_string+=')'
        else:
            new_string+='('
    return new_string

print(duplicate_encode("din")) #  "((("
print(duplicate_encode("recede"))  #"()()()"
print(duplicate_encode("Success"))  # ")())())"
print(duplicate_encode("(( @"))  #"))(("