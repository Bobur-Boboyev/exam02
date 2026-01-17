def calculate(num1: float, num2: float, oper) -> float:
    operators = ['+', '-', '/', '*']

    if oper not in operators:
        return "Error: Noto'g'ri operator"
    elif num2 == 0 and oper == '/':
        return "Error: Nolga bo'lish mumkin emas"
    elif oper == "+":
        return round(num1 + num2, 2)
    elif oper == '-':
        return round(num1 - num2, 2)
    elif oper == '/':
        return round(num1 / num2, 2)
    elif oper == "*":
        return round(num1 * num2, 2)
    

print(calculate(15, 3, '/'))
print(calculate(8, 5, '*'))
print(calculate(10, 0, '/'))
print(calculate(7, 4, '^'))