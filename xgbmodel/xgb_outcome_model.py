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

        # Select the data (use only patients arriving by ambulance)
        mask = self.globvars.data['arrive by ambulance'] == 1
        self.data = \
            self.globvars.data[mask][self.globvars.xgb_thrombolysis_features]