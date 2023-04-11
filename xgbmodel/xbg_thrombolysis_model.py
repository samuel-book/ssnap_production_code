"""
XGBoost machine learning model for stroke thrombolysis prediction.
SHAP values are used to explain the model's predictions.

ToDo:
Measure accuracy with k-fold cross validation.
"""

from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier

from globvars.globvars import GlobVars


class XGBThrombolysisModel(object):
    """
    XGBoost moodel for stroke thrombolysis prediction.
    """

    def __init__(self, globvars) -> None:
        """
        Initialize the XGBoost model.
        """

        # Set up global variables
        self.globvars: GlobVars = globvars

        # Restrict data (e.g. arrive by ambulance)
        # Any need for imputation?

    def split_data_to_X_y(self) -> None:
        """
        Split data into X and y.
        """

        # Split data into X and y
        self.X = self.globvars.restricted_data.drop(columns=['thrombolysis'])
        self.y = self.globvars.restricted_data['thrombolysis']
