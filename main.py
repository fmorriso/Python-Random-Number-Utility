import sys

from random_number_utilities import RandomNumberUtilities


def verify_random_int_works():
    nums = RandomNumberUtilities.random_int(1, 6, 20)
    print(f'nums: {nums}')

def verify_random_float_works():
    max_found = 0
    min_found = sys.float_info.max
    for test in range(100):
        nums = RandomNumberUtilities.random_float_with_tolerance(1, 6, 0.01, 20)
        # print(f'{test} nums: {nums}')
        max_found = max(max_found, nums.max())
        min_found = min(min_found, nums.min())
        filtered_max_values = nums[(nums >= 5.999) & (nums <= 6.001)]
        filtered_min_values = nums[(nums >= 0.999) & (nums <= 1.001)]
        # print(f'filtered_values: {filtered_values}')
        if len(filtered_max_values) > 0:
            print(f'max_found: {max_found} in test {test}')

        if len(filtered_min_values) > 0:
            print(f'min_found: {min_found} in test {test}')


    print(f'min_found: {min_found}, max_found: {max_found}')

def main():
    # verify_random_int_works()
    verify_random_float_works()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

