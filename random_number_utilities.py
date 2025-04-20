from typing import Any

import numpy as np
from numpy import signedinteger, bool, ndarray, dtype, unsignedinteger
from numpy._typing import _64Bit, _8Bit, _16Bit, _32Bit
class RandomNumberUtilities:

    @staticmethod
    def random_int(min_value: int, max_value: int, size: int = 1):
        rng = np.random.default_rng()  # Create an instance of Generator
        return rng.integers(min_value, max_value + 1, dtype = np.int32, size = size)


    @staticmethod
    def random_float(min_value: float, max_value: float, size: int = 1):
        tolerance: float = (max_value - min_value) / 10_000
        return RandomNumberUtilities.random_float_with_tolerance(min_value, max_value, tolerance, size)

    @staticmethod
    def random_float_with_tolerance(min_value: float, max_value: float, tolerance:float = 0.01, size: int = 1):

        if tolerance < 0.0 or tolerance is None:
            tolerance = (max_value - min_value) / 10_000
        return np.random.Generator.floating(min_value, max_value + 1, dtype = np.float32, size = size)