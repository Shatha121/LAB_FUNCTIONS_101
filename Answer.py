def tringle(x: int):
    for num in range(x, 0, -1):
        for num2 in range(num, 0, -1):
            print(num2, end=" ")
        print()

tringle(10)


