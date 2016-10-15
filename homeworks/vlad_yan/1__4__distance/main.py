import math
from optparse import OptionParser
from collections import namedtuple

point = namedtuple('Point', 'x, y')


# Длинные читабельные имена функций это хорошо.
# Короткие не очень читаьбельные - плохо
def dist(a, b):
    """Calculate distance between two points: a and b."""
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def mycartesian_product(some_list):
    """Get cartesian product of a list with itself."""
    pr = []  # Плохое имя
    for ind, item1 in enumerate(some_list[:-1], start=1):
        for item2 in some_list[ind:]:
            pr.append((item1, item2))

    return pr


def xy_from_file(filename):
    """Read in point coordinates from a given file."""
    with open(filename) as fobj:
        content = fobj.readlines()

    try:
        # ValueError может быть пойман только в момент выполннеия float(number)
        # Потому в try...except лучше заключить только его
        splited = [line.split() for line in content]
        points = [point(float(x), float(y)) for x, y in splited]
    except ValueError:
        return None

    return points


def main(filename='test_file.txt'):
    """Main function."""
    points = xy_from_file(filename)
    cartesian_prod = mycartesian_product(points)
    distances = [dist(p1, p2) for p1, p2 in cartesian_prod]

    min_ = min(distances)
    max_ = max(distances)

    print('min: %s\nmax: %s' % (min_, max_))


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()
    if not args:
        main()
    else:
        main(args[0])
