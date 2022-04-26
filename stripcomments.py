def main(text, comms):
    lines = text.split("\n")
    ans = [None] * len(lines)
    print(ans)

    # print(ans)
    # print(lines)


if __name__ == '__main__':
    main("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
