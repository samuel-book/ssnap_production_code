"""
XGBoost machine learning model for stroke outcome prediction.
SHAP values are used to explain the model's predictions.
"""


from globvars.globvars import GlobVars


class XGBOutcomeModel(object):
    """
    XGBoost model for stroke outcome prediction.
    """

    def __init__(self, globvars) -> None:
        """
        Initialize the XGBoost model.
        """

        # Set up global variables
        self.globvars: GlobVars = globvars

        # Restrict data (e.g. arrive by ambulance)
        # Any need for imputation?
