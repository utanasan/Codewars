#Your task is to make a function that can take any non-negative integer
# as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    list_num = [int(num) for num in str(num)]
    sort_list_num = sorted(list_num, reverse=True)
    str_result = int("".join(list(map(str,sort_list_num))))
    return str_result


print(descending_order(125551455555889))


