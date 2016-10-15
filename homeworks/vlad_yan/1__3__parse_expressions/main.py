import re
from optparse import OptionParser

"""
PEP8
Защита от дурака
синтаксис в test.py

Посмотри на результаты анализатора кода в pylint_result, исправь
Добавь вычисление строк типа a + (b *a) - b или a-b+a*a
"""


floatnumber = '\d+(?:\.\d+)?'
myregex = '(?P<operand1>{number})\s*(?P<operation>[\+\-\*/])\s*(?P<operand2>{number})'.format(number=floatnumber)
myre = re.compile(myregex)  # Неудачное название переменной myre. Здесь и ниже


def find_expressions(myre_, string):  # Нижние подчеркивания нужны если работаем с private атрибутами класса.
    expressions = myre_.findall(string)

    return expressions


def evaluate_expression(expression):
    operand1, operation, operand2 = expression
    operand1 = float(operand1)
    operand2 = float(operand2)

    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        result = operand1 / operand2
    else:
        print('ERROR: unknown operation!')
        return

    expr_str = ''.join(expression)
    print('%s = %s' % (expr_str, result))


def main(myre_, string):
    expressions = find_expressions(myre_, string)

    for expr in expressions:
        evaluate_expression(expr)


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()

    arg = args[0]
    main(myre, arg)
