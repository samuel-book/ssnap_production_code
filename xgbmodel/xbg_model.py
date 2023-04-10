"""
XGBoost machine learning model for stroke thrombolysis prediction.
SHAP values are used to explain the model's predictions.
"""

from globvars import GlobVars


class XGBModel(object):
    """
    XGBoost moodel for stroke thrombolysis prediction.
    """

    def __init__(self, globvars) -> None:
        """
        Initialize the XGBoost model.
        """

        # Set up global variables
        self.globvars: GlobVars = globvars
