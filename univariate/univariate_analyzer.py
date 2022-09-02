"""
    Univariate Time Series Analyzer module
"""

import pandas as pd
from typing import Optional, List
from univariate.hook import Hook
from univariate.analyzer import AnalysisReport, Analyzer, RegularityAnalyzer


class UnivariateAnalyzer:
    """
    Univariate Time Series Analyzer
    """

    def __init__(self, ts: pd.DataFrame, hooks=Optional[List[Hook]]):
        """

        :param ts: pandas dataframe that has Datatime index, and has one timeseries value(float or number) series
        :param hooks:
        """
        self.ts: pd.DataFrame = ts
        self.hooks: List[Hook] = hooks or []  # todo : default post analysis hook
        try:
            self.__validate_ts()
        except Exception as e:
            print(
                f"Error in validation ts, ts must be pandas dataframe that has Datatime index, and has one timeseries value(float or number) series"
            )
            raise e
        else:
            self.analysis_queue: List[Analyzer] = list()
            regularity_analyzer: Analyzer = RegularityAnalyzer()
            self.regularity_report: AnalysisReport = regularity_analyzer.analyze()
            self.__notify_report(self.regularity_report)
            self.__enqueue_analysis_job(AnalysisReport["regular_type"])

    def __validate_ts(self) -> bool:
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
