"""
 Descriptive Statistics analyzer
"""

from univariate.analyzer import Analyzer, AnalysisReport
import logging

logger = logging.getLogger()


class DescriptiveStatAnalyzer(Analyzer):
    """
    Descriptvie Statistics analyzer
    Items
      - count
      - mean (arithmetic, geometric, harmonic)
      - mode, median
      - max, min
      - std dev
      - skewness
      - kurtosis
      - coefficient of variation
    """

    def __init__(self):
        """ """

    def analyze(self) -> AnalysisReport:
        """

        :return:
        """
        # 1. count
        # 2. histogram
        # 3. max, min (+ sdev graph)
        # 4. mean, mode, median (+skewness graph)
        # 5. sdev
        # 5. skewness
        # 6. kurtosis
        # 7. coefficient of variation
