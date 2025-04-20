import sys

from random_number_utilities import RandomNumberUtilities


def verify_random_int_works():
    min_value: int = 1
    max_value: int = 6

    max_found: int = 0
    min_found: int = sys.maxsize
    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}
    for test in range(1_000):
        nums = RandomNumberUtilities.random_int(min_value, max_value, 20)
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
    print(f'{frequency = }')


def verify_random_float_with_tolerance_works():
    min_value: float = 1.0
    max_value: float = 6.0

    max_found: float = 0
    min_found: float = sys.float_info.max
    # keep track of how many times the min_value and max_value were generated
    frequency =   {'min': 0, 'max': 0}
    for test in range(1_000):
        nums = RandomNumberUtilities.random_float_with_tolerance(1, 6, 0.01, 20)
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
    print(f'{frequency = }')

def verify_random_float_works():
    min_value = 1.0
    max_value = 6.0

    max_found = 0
    min_found = sys.float_info.max

    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}

    for test in range(10_00):
        nums = RandomNumberUtilities.random_float(min_value, max_value, 20)

        # print(f'{test} nums: {nums}')
        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())

        # print(f'test: {test}:  {min_found = }, {max_found = }')
        if max_found == max_value:
            frequency['max'] += 1
        if min_found == min_value:
            frequency['min'] += 1

    print(f'min_found: {min_found}, max_found: {max_found}')
    print(f'{frequency = }')


def main():
    verify_random_int_works()
    verify_random_float_works()
    verify_random_float_with_tolerance_works()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

