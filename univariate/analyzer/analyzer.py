"""

"""

from abc import ABCMeta, abstractmethod
from univariate.analyzer import AnalysisReport


class Analyzer(metaclass=ABCMeta):
    """
    Abstract analyzer for analyzing with specific strategy.
    """

    @abstractmethod
    def analyze(self) -> AnalysisReport:
        """
            Command Executor
        :return:
        """
        pass
