#gives us the highest and lowest muber entered in a list

def hilo(list_of_nums):

    high = float("-inf")
    low = float("inf")
    for index in range(0, len(list_of_nums)):
        if list_of_nums[index] > high:
            high = list_of_nums[index]
        if list_of_nums[index] < low:
            low = list_of_nums[index]
    return high, low

high, low = hilo([5, 3, 1, 2, 3, 5, 10, 15, 20, 25, 0])
print(high, low)