def main():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    m = [str(a) for a in n]
    x1 = "".join(m[0:3])
    x2 = "".join(m[3:6])
    x3 = "".join(m[6:])
    print(x1, x2, x3)
    r = f"({x1}) {x2}-{x3}"
    print(r)

main()
