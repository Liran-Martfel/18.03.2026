def safe_open():
    """
    checking if the code of the safe is correct
    """
    secret_code = [77, 12, 43, 100, 51]
    try_number = int(input('enter the first code: '))
    i = 0
    while True:
        try:
            if secret_code[i] == try_number:
                if try_number == 51:
                    print('The safe is open')
                    break
                else:
                    try_number = int(input('Correct number, try the next one: '))
                    i += 1
            else:
                try_number = int(input('Wrong number, try Again: '))
                i = 0
        except IndexError as e:
            print('Invalid number',e)
        except ValueError as e:
            print('Invalid number',e)
safe_open()
