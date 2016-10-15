import re
from optparse import OptionParser  # Deprecated lib (https://docs.python.org/3/library/optparse.html)


def number_of_brackets(string, brackets):
    """Get total number of brackets in a string."""
    myregex = '[%s]' % ''.join(['\%s\%s' % (item[0], item[1]) for item in brackets])
    result = re.findall(myregex, string)

    return len(result)


def check_brackets(string, open_bracket, close_bracket):
    """
    Check if the string contains a consistent set of brackets.
    If it does - return None, if it does't - return the position
    of the wrong bracket."""
    open_count = 0  # opening brackets counter
    close_count = 0  # closing brackets counter

    # Лучше назвать переменную index, чем ind.
    # Длинные названия переменных - добро, если они информативны
    # ind не очень хорошо потому что для того чтобы понять что оно значит нужно дочитать до enumerate
    for ind, char in enumerate(string):
        if char == open_bracket:
            open_count += 1
        elif char == close_bracket:
            close_count += 1

        if close_count <= open_count:
            continue

        return ind

    if close_count != open_count:
        return -1
    else:
        return None


def main(string):
    """Main function."""
    brackets = [
        ('(', ')'),
        ('[', ']'),
        ('{', '}')
    ]

    status = True
    bad_bracket = None

    for open_bracket, close_bracket in brackets:
        ind = check_brackets(string, open_bracket, close_bracket)
        if ind is not None:
            if ind == -1:
                bad_bracket = -1
            else:
                bad_bracket = number_of_brackets(string[:ind], brackets) + 1
            status = False
            break

    if status:
        print('yes')
    else:
        print(bad_bracket)


if __name__ == '__main__':
    optparser = OptionParser()
    opts, args = optparser.parse_args()

    arg = args[0]

    """
    Добавь проверки - если скрипту ничего не передать - он валится с IndexError-ом
    Если передать число или строку типа ".*-+" - получим yes

    Если передать строку обычную - то все ок.

    Попробуй упростить решение, избавиться от лишних флагов, переменных
    Исправь замечания, запушь в свой репозиторий

    """

    main(arg)
