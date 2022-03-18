def main(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


if __name__ == '__main__':
    print(f"Expected: 3  | Received: {main([1, 2, 3, 4, 3, 2, 1])}")
    print(f"Expected: 1  | Received: {main([1, 100, 50, -51, 1, 1])}")
    print(f"Expected: -1 | Received: {main([1,2,3,4,5,6])}")
    print(f"Expected: 0  | Received: {main([20,10,-80,10,10,15,35])}")
