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
    print(f"mot donné : {word} et mot retour : {ret}")


if __name__ == '__main__':
    main("bonjour")
    main("din")
    main("recede")
    main("Success")
    main("(( @")
    main("bbb")
