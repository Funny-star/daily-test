a = float(input('num1 :'))
b = float(input('num2 :'))
c = input('ope :')


def run(a, b, c):
    match c:
        case'+':
            result = a + b
        case'-':
            result = a - b
        case'*':
            result = a * b
        case'/':
            result = a / b
        case _:
            result = None
    return result


print(run(a, b, c))
