def main(word):
    letters = dict()
    word = word.lower()
    ret = ""
    for w in word:
        if w in letters:
            letters[w] = ')'
        else:
            letters[w] = '('
    for w in word:
        ret += letters[w]
    return ret


if __name__ == '__main__':
    main("din")
    main("recede")
    main("Success")
    main("(( @")

