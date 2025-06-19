def tringle(x: int):
    final_rounds = ""
    for num in range(x, 0, -1):
        for num2 in range(num, 0, -1):
            rounds = str(num2) + " "
            final_rounds +=rounds
        final_rounds += "\n"
    return final_rounds
                
print(tringle(10))
