#Mean, median, mode, and range

def mean(lst):
    return sum(lst) / len(lst)


def rnge(lst):
    lst.sort()
    return lst[len(lst) - 1] - lst[0]


def median(lst):
    print(lst)
    #for even number of entries
    if len(lst) % 2 == 0:
        return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2
    #odd number of entries
    else:
        return lst[int(len(lst) / 2)]

def mode(lst):
    mode_num = lst[0]
    mode_count_max = 1
    for num in lst:
        if lst.count(num) > mode_count_max:
            mode_num = num
            mode_count_max = lst.count(num)
        if mode_count_max == 1:
            return None
        else:
            return mode_num, mode_count_max

sample_data = [5, 6, 0, 10, 9]
print("Mean: " + str(mean(sample_data)))
print("Range: " + str(rnge(sample_data)))
print("Median: " + str(median(sample_data)))
print("Mode: " + str(mode(sample_data)))
