"""
    Univariate Time Series Analyzer module
"""

from pyspark.sql import DataFrame
from typing import Optional, List
from univariate.hook import Hook
from univariate.analyzer import AnalysisReport, Analyzer, RegularityAnalyzer


class UnivariateAnalyzer:
    """
    Univariate Time Series Analyzer
    """

    def __init__(
        self,
        ts: DataFrame,
        val_col: str = "value",
        time_col: str = "time",
        hooks=Optional[List[Hook]],
    ):
        """

        :param ts: Spark dataframe that has one datatime column, and has one timeseries value(float or number) column
        :param val_col: string column name containing timeseries values
        :param time_col: string column name containing pyspark.sql.DatetimeType
        :param hooks: list of hooks that want to be notified analysis reports
        """
        self.ts: DataFrame = ts
        self.hooks: List[Hook] = hooks or []  # todo : default post analysis hook
        try:
            self.__validate_ts(val_col, time_col)
        except Exception as e:  # todo: Custom exception or specific
            print(
                "Error in validation ts, ts must be pyspark sql dataframe that has one DatatimeType column, "
                "and has one timeseries value(float or number) column"
            )
            raise e
        else:
            self.analysis_queue: List[Analyzer] = list()
            regularity_analyzer: Analyzer = RegularityAnalyzer()
            self.regularity_report: AnalysisReport = regularity_analyzer.analyze()
            self.__notify_report(self.regularity_report)
            self.__enqueue_analysis_job(AnalysisReport["regular_type"])

    def __validate_ts(self, val_col: str, time_col: str) -> bool:
        pass

    def __notify_report(self, report: AnalysisReport):
        map(lambda hook: hook.do_post_analysis(report), self.hooks)

    def __enqueue_analysis_job(self):
        """

        :param regular_type:
        :return:
        """
        if self.regularity_report["regular_type"] == "regular":
            pass
        elif self.regularity_report["regular_type"] == "irregular":
            pass
