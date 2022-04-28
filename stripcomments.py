def main(string, markers):
    lines = string.split("\n")
    ans = [line.strip() for line in lines]
    print(ans)
    for idx, line in enumerate(lines):
        for marker in markers:
            if marker in line:
                if line[-1] == marker:
                    ans[idx] = line[:-1].strip()
                elif line[0] == marker:
                    ans[idx] = None
                else:
                    ans[idx] = line.split(marker)[0].strip()
    print(ans)
    return "\\n".join(ans)


if __name__ == '__main__':
    # print(main("apples, pears # and bananas\ngrapes \nbananas !apples", ["#", "!"]))
    # print(main("a #b\nc\nd $e f g", ["#", "$"]))
    # print(main("apples, pears\ngrapes\nbananas #", ["#"]))
    print(main("strawberries watermelons ? avocados\n!\n' cherries . oranges oranges", ["'", '?', '.', '#', '^']))
    # print(main('lemons\nbananas\n? strawberries pears @ pears apples', ['!', '?', '.', '^', '#', '-', '@', '=', ',']))
