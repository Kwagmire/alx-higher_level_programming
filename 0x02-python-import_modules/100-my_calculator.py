#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    len = len(sys.argv)
    operators = ["+", "-", "*", "/"]
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]

    if len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    match sys.argv[2]:
        case "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
