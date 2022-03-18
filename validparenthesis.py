def main(string):
    if not string:
        return True
    else:
        par = []
        for c in string:
            if c == "(":
                par.append("(")
            if c == ")":
                if not par:
                    return False
                elif par.pop() == ")":
                    return False
        return True if not par else False


if __name__ == '__main__':
    test = [
        "  (",  # False
        ")test",  # False
        "",  # True
        "hi())(",  # False
        "hi(hi)()"  # True
    ]
    for t in test:
        if main(t):
            print(f"Test {t} is True")
        else:
            print(f"Test {t} is False")
