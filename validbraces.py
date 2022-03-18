def main(string):
    val = []
    for c in string:
        try:
            if c in ["(", "{", "["]:
                val.append(c)
            elif c == ")":
                if val.pop() != "(":
                    return False
            elif c == "]":
                if val.pop() != "[":
                    return False
            elif c == "}":
                if val.pop() != "{":
                    return False
        except IndexError:
            return False
    return True if not val else False


if __name__ == "__main__":
    print("True" if main("[]") else "False")
