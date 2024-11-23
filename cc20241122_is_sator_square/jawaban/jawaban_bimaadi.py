from typing import List
from unittest import TestCase


def scan_horizontal(tablet: List[List[str]]) -> List[str]:
    result = []
    for item in tablet:
        result.append("".join(item))
    return result


def scan_horizontal_reverse(tablet: List[List[str]]) -> List[str]:
    result = []
    for item in reversed(tablet):
        result.append("".join(item[::-1]))
    return result


def scan_vertical(tablet: List[List[str]]) -> List[str]:
    result = []
    for idx in range(len(tablet[0])):
        temp = []
        for item in tablet:
            temp.append(item[idx])

        result.append("".join(temp))
    return result


def scan_vertical_reverse(tablet: List[List[str]]) -> List[str]:
    result = []
    for idx in range(len(tablet[0]) - 1, -1, -1):
        temp = []
        for item in tablet:
            temp.append(item[idx])
        result.append("".join(temp[::-1]))

    return result


def is_sator_square(tablet: List[List[str]]) -> bool:
    sh = scan_horizontal(tablet=tablet)
    shr = scan_horizontal_reverse(tablet=tablet)
    sv = scan_vertical(tablet=tablet)
    svr = scan_vertical_reverse(tablet=tablet)
    for item in sh:
        if not (item in shr and item in sv and item in svr):
            return False

    return True


def test_1():
    tablet = [["T", "E", "N"], ["E", "Y", "E"], ["N", "E", "T"]]
    res = is_sator_square(tablet=tablet)
    TestCase().assertTrue(res)


def test_2():
    tablet = [["N", "O", "T"], ["O", "V", "O"], ["N", "O", "T"]]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)


def test_3():
    tablet = [
        ["B", "A", "T", "S"],
        ["A", "B", "U", "T"],
        ["T", "U", "B", "A"],
        ["S", "T", "A", "B"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertTrue(res)


def test_4():
    tablet = [
        ["P", "A", "R", "T"],
        ["A", "G", "A", "R"],
        ["R", "A", "G", "A"],
        ["T", "R", "A", "M"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)


def test_5():
    tablet = [
        ["S", "A", "T", "O", "R"],
        ["A", "R", "E", "P", "O"],
        ["T", "E", "N", "E", "T"],
        ["O", "P", "E", "R", "A"],
        ["R", "O", "T", "A", "S"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertTrue(res)


def test_6():
    tablet = [
        ["S", "A", "L", "A", "S"],
        ["A", "R", "E", "N", "A"],
        ["L", "E", "V", "E", "L"],
        ["A", "R", "E", "N", "A"],
        ["S", "A", "L", "A", "S"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)


def test_7():
    tablet = [
        ["B", "A", "T", "S"],
        ["U", "B", "U", "T"],
        ["T", "U", "B", "U"],
        ["S", "T", "A", "B"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)


def test_8():
    tablet = [
        ["S", "A", "T", "O", "R"],
        ["A", "R", "E", "P", "O"],
        ["T", "I", "N", "I", "T"],
        ["O", "P", "E", "R", "A"],
        ["R", "O", "T", "A", "S"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)


def test_9():
    tablet = [
        ["S", "A", "T", "O", "R"],
        ["A", "R", "A", "P", "O"],
        ["T", "E", "N", "E", "T"],
        ["O", "P", "A", "R", "A"],
        ["R", "O", "T", "A", "S"],
    ]
    res = is_sator_square(tablet=tablet)
    TestCase().assertFalse(res)
