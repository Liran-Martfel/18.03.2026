def get_list():
    counting = 0
    for i in range(len(number)):
        if number[i] >= i:
            counting = counting + 1
            if counting == 4:
                print (number[i])
                break
number = [88,100,90,95,97,97,99,97,99]
get_list ()