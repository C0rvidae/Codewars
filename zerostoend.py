def main(array):
    i = 0
    ret = [0] * len(array)
    for c in array:
        if c != 0:
            ret[i] = c
            i += 1
    return ret


if __name__ == '__main__':
    arr = main([1, 0, 1, 2, 0, 1, 3])
    print(arr)
    arr = main([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
    print(arr)
