def first_non_repeating_letter(string):
    chars = dict()
    arr = []
    for idx, c in enumerate(string):
        chars[c.lower()] = idx if c.lower() not in chars else -1
    for k in chars:
        if chars[k] != -1:
            arr.append(chars[k])
    ret = '' if len(arr) == 0 else string[min(arr)]
    return ret


if __name__ == '__main__':
    # a
    first_non_repeating_letter("a")
    # t
    first_non_repeating_letter("stress")
    # e
    first_non_repeating_letter("moonmen")
    # none
    first_non_repeating_letter("abba")
    # none
    first_non_repeating_letter("aa")
    # #
    first_non_repeating_letter("~><#~><")
    # w
    first_non_repeating_letter("hello world, eh?")
    # T
    first_non_repeating_letter("sTreSS")
    # ,
    first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!")
