"""
XGBoost machine learning model for stroke thrombolysis prediction.
SHAP values are used to explain the model's predictions.

ToDo:
Measure accuracy with k-fold cross validation.
"""
import numpy as np
import pandas as pd

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

    def split_data_to_X_y(self) -> None:
        """
        Split data into X and y.
        """

        # Drop rows with onset-to-arrival time of > 240 mins
        mask = self.globvars.restricted_data["onset-to-arrival time"] <= 240
        xgb_data = self.globvars.restricted_data[mask]

        # Only use arrive by ambulance
        xgb_data = xgb_data[xgb_data['arrive by ambulance'] == 1]

        # Use selected fields only
        xgb_data = xgb_data[self.globvars.xgb_thrombolysis_fields]

        # Split data into X and y
        self.X = xgb_data.drop(columns=['thrombolysis'])
        self.y = xgb_data['thrombolysis']

    def create_k_folds(self) -> None:
        """
        Create 5 k-fold for cross-validation.
        """

        # Create stratification based on hospital and thrombolysis use
        stratification: pd.Series = (
            self.globvars.restricted_data['stroke team'] +
            self.globvars.restricted_data['thrombolysis'].astype(str)
        )

        # Create 5 k-fold for cross-validation
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        skf.get_n_splits(self.globvars.restricted_data, stratification.values)

        self.k_fold_train_X = []
        self.k_fold_train_y = []
        self.k_fold_test_X = []
        self.k_fold_test_y = []
        self.k_fold_train_index = []
        self.k_fold_test_index = []

        for k, (train_index, test_index) in enumerate(
                skf.split(self.X, self.y)):
            X_train, X_test = self.X.iloc[train_index], self.X.iloc[test_index]
            y_train, y_test = self.y.iloc[train_index], self.y.iloc[test_index]
            self.k_fold_train_X.append(X_train)
            self.k_fold_train_y.append(y_train)
            self.k_fold_test_X.append(X_test)
            self.k_fold_test_y.append(y_test)
            self.k_fold_train_index.append(train_index)
            self.k_fold_test_index.append(test_index)

            X_train.to_csv(f'./data/k_fold/X_train_{k}.csv', index=False)
            X_test.to_csv(f'./data/k_fold/X_test_{k}.csv', index=False)
            y_train.to_csv(f'./data/k_fold/y_train_{k}.csv', index=False)
            y_test.to_csv(f'./data/k_fold/y_test_{k}.csv', index=False)

    def validate_model(self) -> None:
        """
        Build and test the model.
        """

        # Split data into X and y
        self.split_data_to_X_y()

        # Process data into 5 folds for cross-validation
        self.create_k_folds()

        # Validate using 5-fold cross-validation
        for k in range(5):

            # One hot encode hospitals
            X_train_hosp = (pd.get_dummies(
                self.k_fold_train_X[k]['stroke team'], prefix='team'))
            X_train = pd.concat([self.k_fold_train_X[k], X_train_hosp], axis=1)
            X_train.drop('stroke team', axis=1, inplace=True)
            X_test_hosp = \
                pd.get_dummies(
                    self.k_fold_test_X[k]['stroke team'], prefix='team')
            X_test = pd.concat([self.k_fold_test_X[k], X_test_hosp], axis=1)
            X_test.drop('stroke team', axis=1, inplace=True)

            # Create XGBoost model
            model = XGBClassifier(verbosity=0, seed=42, learning_rate=0.5)
            model.fit(X_train, self.k_fold_train_y[k])

            # Get predictions
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1]
            accuracy = np.mean(y_pred == self.k_fold_test_y[k])
            print(f'Accuracy: {accuracy:.3f}')

            # Get ROC curve
            fpr, tpr, thresholds = \
                roc_curve(self.k_fold_test_y[k], y_pred_proba)
            roc_auc = auc(fpr, tpr)
            print(f'ROC AUC: {roc_auc:.3f}')
