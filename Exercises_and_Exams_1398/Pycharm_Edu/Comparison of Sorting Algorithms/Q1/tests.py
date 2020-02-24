from test_helper import *
from task import *

if __name__ == '__main__':
    tests = [
        (3, 3, [2, 1, 3]),
        (4, 1, [1, 2, 3, 4]),
        (5, 6, -1),
        (100, 100, -1),
        (10, 17, [3, 1, 4, 6, 2, 8, 5, 9, 7, 10]),
        (20, 15, [3, 1, 4, 6, 2, 5, 8, 7, 9, 11, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        (30, 17,
         [2, 4, 1, 6, 3, 8, 5, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30]),
        (80, 25,
         [3, 1, 4, 6, 2, 8, 5, 9, 11, 7, 10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]),
        (120, 66, -1)

    ]
    for test in tests:
        test_function(test[-1], func, test[0], test[1])
