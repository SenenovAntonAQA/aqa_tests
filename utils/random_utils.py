import random

class RandomUtils:
    @staticmethod
    def get_random_value_in_range(min_val, max_val, step=1):
        steps = int((max_val - min_val) / step)
        random_step = random.randint(0, steps)
        return min_val + random_step * step