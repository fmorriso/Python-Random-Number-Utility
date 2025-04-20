import sys

from random_number_utilities import RandomNumberUtilities


def verify_random_int_works():
    for test in range(100):
        nums = RandomNumberUtilities.random_int(1, 6, 20)
        print(f'nums: {nums}')


    # keep track of how many times the min_value and max_value were generated
    frequency = {'min': 0, 'max': 0}

def verify_random_float_with_tolerance_works():
    max_found: float = 0
    min_found: float = sys.float_info.max
    # keep track of how many times the min_value and max_value were generated
    frequency =   {'min': 0, 'max': 0}
    for test in range(1_000):
        nums = RandomNumberUtilities.random_float_with_tolerance(1, 6, 0.01, 20)
        # print(f'{test} nums: {nums}')
        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())
        filtered_max_values = nums[(nums >= 5.999) & (nums <= 6.001)]
        filtered_min_values = nums[(nums >= 0.999) & (nums <= 1.001)]
        # print(f'filtered_values: {filtered_values}')
        if len(filtered_max_values) > 0:
            #print(f'max_found: {max_found} in test {test}')
            frequency['max'] += 1

        if len(filtered_min_values) > 0:
            #print(f'min_found: {min_found} in test {test}')
            frequency['min'] += 1


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

