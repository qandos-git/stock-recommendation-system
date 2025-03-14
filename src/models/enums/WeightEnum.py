from enum import Enum

class WeightEnum(Enum):
    POSITIVE_NEWS = 1.0
    NEUTRAL_NEWS = 0.0
    NEGATIVE_NEWS = -1.0
