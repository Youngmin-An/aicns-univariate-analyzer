"""

"""

from abc import ABCMeta, abstractmethod
from univariate.analyzer import AnalysisReport
from typing import Dict, Optional
from enum import Enum


class Analyzer(metaclass=ABCMeta):
    """
    Abstract analyzer for analyzing with specific strategy.
    """

    @abstractmethod
    def __init__(self, strategies: Optional[Dict[str, Enum], None]):
        pass

    @abstractmethod
    def analyze(self) -> AnalysisReport:
        """
            Command Executor
        :return:
        """
        pass
