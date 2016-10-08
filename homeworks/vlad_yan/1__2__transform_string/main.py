# -*- coding: utf-8 -*-
import re
from optparse import OptionParser


def isurl(string):
    """Check whether the given string is a valid url address."""
    length = len(string)
    if length < 8:
        return False

    ind = string.find('http://')
    if ind != 0:
        ind = string.find('https://')
        if not (ind == 0 and length >= 9):
            return False

    return True


def isemail(string):
    """Check whether the given string is a valid email address."""
    if len(string) < 5 or '@' not in string[1:-1]:
        return False
    parts = string.split('@')
    if len(parts) != 2:
        return False

    part1, part2 = parts

    if len(part2) < 3 or '.' not in part2[1:-1]:
        return False

    another_parts = part2.split('.')
    if len(another_parts) != 2:
        return False

    return True


def retrieve_spaces(string):
    spaces = []
    if ' ' not in string:
        return spaces

    numofspaces = []
    while True:
        ind = string.find(' ')

        if ind == -1:
            break

        n = 0
        for char in string[ind:]:
            if char == ' ':
                n += 1
            else:
                break

        numofspaces.append(n)
        string = string[ind+n:]

    for n in numofspaces:
        spaces.append(' '*n)

    return spaces


def isnumber(char):
    """Check whether char is a number."""
    for ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if ch == char:
            return True

    return False


def islongnumber(string):
    """Check whether string is a N-figure number (N >= 3)."""
    if len(string) < 3:
        return False

    for char in string:
        if not isnumber(char):
            return False

    return True


def regex_transform(string):
    urlregex = 'https?://[^\s]+'
    emailregex = '[^@^\s]+@[^@^\s]+\.[^@^\s]+'
    numbersregex = '[0-9]{3,}'

    string = re.sub(urlregex, '[ссылка запрещена]', string)
    string = re.sub(emailregex, '[контакты запрещены]', string)
    string = re.sub(numbersregex, '', string)

    # first character must be UPPER case
    string = string[0].upper() + string[1:]

    # the rest of the string must be lower case
    string = string[0] + re.sub('[A-Z]', lambda m: m.group(0).lower(), string[1:])

    return string


def simple_transform(string):
    words = string.split()
    spaces = retrieve_spaces(string)

    for ind, word in enumerate(words):
        if isurl(word):
            words[ind] = '[ссылка запрещена]'
            continue
        elif isemail(word):
            words[ind] = '[контакты запрещены]'
            continue
        elif islongnumber(word):
            words[ind] = ''
            continue

        words[ind] = word.lower()

    first_word = words[0]
    words[0] = first_word[0].upper() + first_word[1:]

    result = ''

    spaces.append('')
    for word, sp in zip(words, spaces):
        result += (word + sp)

    return result


def main(string, useregex=True):
    """
    Transform the given string.
    useregex - regular expressions usage flag."""
    if useregex:
        result = regex_transform(string)

    else:
        result = simple_transform(string)

    return result


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()

    arg = args[0]
    newstr = main(arg, useregex=False)

    print(newstr)
