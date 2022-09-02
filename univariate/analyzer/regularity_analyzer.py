"""

"""

from univariate.analyzer import Analyzer
from univariate.analyzer import AnalysisReport
from univariate.strategy.agreement import AgreementStrategy, AgreementType
from typing import Dict, Optional
from enum import Enum
import importlib


class RegularityAnalyzer(Analyzer):
    """ """

    def __init__(self, strategies: Optional[Dict[str, Enum], None]):
        agreement_strategy_type = (
            strategies.get("agreement", AgreementType.BLAND_ALTMAN)
            if strategies is not None
            else AgreementType.BLAND_ALTMAN
        )
        concrete_cls = getattr(
            importlib.import_module("univariate.strategy.agreement"),
            agreement_strategy_type.value,
        )
        self.agreement_strategy: AgreementStrategy = concrete_cls()

    def analyze(self) -> AnalysisReport:
        pass
