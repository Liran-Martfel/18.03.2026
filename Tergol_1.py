number = int(input("enter a number between 1 and 9: "))
number_1 = []
for num in range(1,number + 1):
    number_1.append(num)
    print(str(number_1)[1:-1])
    if num == number:
        for num_1 in range(len(number_1)-1):
            number_1.remove(number - num_1)
            print(str(number_1)[1:-1])

j = 1
for num in range(1,number + 1):
    print(" " * (number - num), end="")
    print('*' * j)
    j += 2