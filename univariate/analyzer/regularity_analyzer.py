"""

"""

from univariate.analyzer import Analyzer
from univariate.analyzer import AnalysisReport
from univariate.strategy.agreement import AgreementStrategy, AgreementType
from typing import Dict, Optional
from enum import Enum
import importlib
from pyspark.sql import DataFrame
from pyspark.sql.window import Window
import pyspark.sql.functions as F


class RegularityAnalyzer(Analyzer):
    """ """

    def __init__(
        self, agreement_strategy_type: AgreementType = AgreementType.BLAND_ALTMAN
    ):
        """

        :param agreement_strategy_type: Enum val for agreement strategy, default BLAND_ALTMAN
        """
        concrete_cls = getattr(
            importlib.import_module("univariate.strategy.agreement"),
            agreement_strategy_type.value,
        )
        self.agreement_strategy: AgreementStrategy = concrete_cls()

    def analyze(self, ts: DataFrame, time_col_name: str) -> AnalysisReport:
        """

        :param ts: Time series spark dataframe containing timestamp, data
        :param time_col_name:
        :return:
        """
        differenced_timestamp = self.__make_difference_series_of_timestamp(
            ts, time_col_name
        )
        return self.agreement_strategy.measure_agreement(differenced_timestamp)

    def __make_difference_series_of_timestamp(
        self, ts: DataFrame, time_col_name: str
    ) -> DataFrame:
        window = Window.partitonBy().orderBy(time_col_name)
        diff_col_name = time_col_name + "_diff"
        return (
            ts.withColumn(
                diff_col_name,
                F.col(time_col_name) - F.lag(F.col(time_col_name), 1).over(window),
            )
            .select(diff_col_name)
            .na.drop()
        )  # todo : think less column exception
