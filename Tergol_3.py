def if_sorted():
    if l1st == sorted(l1st):
        return True
    else:
        return False

l1st = [1,2,3,4,9,6,7,5,9]
if if_sorted():
    print('sorted')
else:
    print('not sorted')
