"""

"""

from abc import ABCMeta, abstractmethod
from enum import Enum
import numpy as np


class AgreementType(Enum):
    BLAND_ALTMAN = "BlandAltmanPlot"


class AgreementStrategy(metaclass=ABCMeta):
    """
    Abstract strategy for making a decision that sample set values are agreed.
    """

    @classmethod
    def is_agreed(cls, sample: np.array) -> bool:
        pass
