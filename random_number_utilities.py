from typing import ClassVar

import numpy as np


class RandomNumberUtilities:
    """
    A random number utility that INCLUDES both the minimum and maximum values,
    unlike default python which fails to include the maximum value when generating
    random numbers.
    """
    rng: ClassVar[np.random.Generator] = np.random.default_rng()


    @staticmethod
    def random_int(min_value: int, max_value: int, size: int = 1):
        return RandomNumberUtilities.rng.integers(min_value, max_value + 1, dtype = np.int32, size = size)


    @staticmethod
    def random_float(min_value: float, max_value: float, size: int = 1):
        # print(f'tolerance: {tolerance}')
        return RandomNumberUtilities.random_float_with_tolerance(min_value, max_value, size)


    @staticmethod
    def random_float_with_tolerance(min_value: float, max_value: float, size: int = 1, tolerance: float = None):
        if tolerance is None:
            tolerance = (max_value - min_value) / 10_000
        # print(f'tolerance: {tolerance}')
        extended_min_value = min_value - tolerance
        extended_max_value = max_value + tolerance
        extended_range = extended_max_value - extended_min_value
        nums = np.array([], dtype = np.float64)
        for i in range(size):
            num = RandomNumberUtilities.rng.random(size = 1) * extended_range + extended_min_value
            if num < min_value:
                num = min_value
            elif num > max_value:
                num = max_value

            nums = np.append(nums, np.float64(num))

        return nums
