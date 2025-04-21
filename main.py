import sys

import numpy as np

from random_number_utilities import RandomNumberUtilities


def verify_random_int_works(num_tests: int = 100, test_size: int = 20):
    min_value: int = 1
    max_value: int = 6

    max_found: int = -sys.maxsize
    min_found: int = sys.maxsize

    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}

    for test in range(num_tests):
        nums = RandomNumberUtilities.random_int(min_value, max_value, test_size)
        # print(f'nums: {nums}')

        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())

        min_matches = nums[nums == min_value]
        if len(min_matches) > 0:
            frequency['min'] += len(min_matches)

        max_matches = nums[nums == max_value]
        if len(max_matches) > 0:
            frequency['max'] += len(max_matches)

    print(f'min_found: {min_found}, max_found: {max_found}')
    print(f'{num_tests = }, {test_size = }, {frequency = }')


def verify_random_float_with_tolerance_works(num_tests: int = 1_000, test_size: int = 20):
    min_value: float = 1.0
    max_value: float = 6.0
    tolerance: float = 0.3

    max_found: float = sys.float_info.min
    min_found: float = sys.float_info.max

    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}
    for test in range(num_tests):
        nums = RandomNumberUtilities.random_float_with_tolerance(min_value, max_value, test_size, tolerance)
        # print(f'{test} nums: {nums}')
        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())

        min_matches = nums[nums == min_value]
        if len(min_matches) > 0:
            frequency['min'] += len(min_matches)

        max_matches = nums[nums == max_value]
        if len(max_matches) > 0:
            frequency['max'] += len(max_matches)

    print(f'min_found: {min_found}, max_found: {max_found}')
    print(f'{num_tests = }, {test_size = }, {frequency = }')


def verify_random_float_works(num_tests: int = 1_000, test_size: int = 20):
    min_value: float = 1.0
    max_value: float = 6.0

    max_found: float = sys.float_info.min
    min_found: float = sys.float_info.max

    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}

    for test in range(1_000):
        nums = RandomNumberUtilities.random_float(min_value, max_value, test_size)

        # print(f'{test} nums: {nums}')
        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())

        min_matches = nums[nums == min_value]
        if len(min_matches) > 0:
            frequency['min'] += len(min_matches)

        max_matches = nums[nums == max_value]
        if len(max_matches) > 0:
            frequency['max'] += len(max_matches)

    print(f'min_found: {min_found}, max_found: {max_found}')
    print(f'{num_tests = }, {test_size = }, {frequency = }')


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_numpy_version() -> str:
    return f'{np.__version__}'


def main():
    verify_random_int_works()
    verify_random_float_works()
    verify_random_float_with_tolerance_works()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'NumPy version: {get_numpy_version()}')
    main()
