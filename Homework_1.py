def is_n_biggest(list_of_numbers: list, n: int):
    """
    :param list list_of_numbers: list of numbers
    :param int n: ranked number
    return: the - n-th biggest number
    """
    while n > 0:
        no_double_numb = []
        for num in list_of_numbers:
            if num in no_double_numb:
                continue
            else:
                no_double_numb.append(num)
        if n > len(no_double_numb):
            return f'n-th biggest number is: {max(no_double_numb)}'
        sorted_list = sorted(no_double_numb)
        return sorted_list[-n]
    else:
        return None

number = input("Please enter a number: ")
while not number.isdigit():
    number = input("Please enter a number: ")
n = int(number)
list_of_numbers = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(is_n_biggest(list_of_numbers, n))