"""
    Univariate Time Series Analyzer module
"""

from pyspark.sql import DataFrame
from typing import Optional, List
from univariate.hook import Hook
from univariate.analyzer import AnalysisReport, Analyzer, RegularityAnalyzer
import logging

logger = logging.getLogger()


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
        logger.debug(
            f"Setup Analyzer start, ts: {ts}, val_col: {val_col}, time_col: {time_col}, hooks: {hooks or '[]'}"
        )
        self.ts: DataFrame = ts
        self.hooks: List[Hook] = hooks or []  # todo : default post analysis hook
        self.analysis_queue: List[Analyzer] = list()
        try:
            self.__validate_ts(val_col, time_col)
        except Exception as e:  # todo: Custom exception or specific
            logger.error(
                "Error in validation ts, ts must be pyspark sql dataframe that has one DatatimeType column, "
                "and has one timeseries value(float or number) column"
            )
            raise e
        else:
            regularity_analyzer: Analyzer = RegularityAnalyzer()
            self.regularity_report: AnalysisReport = regularity_analyzer.analyze(
                ts=self.ts, time_col_name=time_col
            )
            self.__notify_report(self.regularity_report)
            self.__enqueue_analysis_job()

    def __validate_ts(self, val_col: str, time_col: str) -> bool:
        pass

    def __notify_report(self, report: AnalysisReport):
        map(lambda hook: hook.do_post_analysis(report), self.hooks)
        logger.debug("Notify all hook")

    def __enqueue_analysis_job(self):
        """

        :return:
        """
        logger.debug("enqueue analysis job start")
        if self.regularity_report.regularity == "regular":
            pass
        elif self.regularity_report.regularity == "irregular":
            pass

    def analyze(self):
        """

        :return:
        """
        logger.debug("analyze called")
        map(
            lambda job: map(
                lambda hook: hook.do_post_analysis(job.analyze), self.hooks
            ),
            self.analysis_queue,
        )  # todo : Explore parallezing with spark sub(child) context?
