import pandas as pd

from typing import Any


class GlobVars:
    """
    Object to store global variables
    """

    def __init__(self, *args: Any, **kwargs: Any):
        """
        Initialize the global variables object.

        Parameters
        ----------

        excluded_teams: list
            The list of stroke teams excluded from the analysis, as obtained by
            applying prescribed limits to the data.

        included_teams: list
            The list of stroke teams included in the analysis, as obtained by
            applying prescribed limits to the data.

        minimum_admissions_per_year: float
            The minimum number of admissions per year to be included in the
            analysis.

        minimum_thrombolysis_per_year: float
            The minimum number of thrombolysis per year to be included in the
            analysis.

        refit_ml_models: bool
            Whether to refit the machine learning models.

        year_end: int
            The last year of the data to be used in the analysis.

        year_start: int
            The first year of the data to be used in the analysis.
        """

        self.excluded_teams: list = []
        self.included_teams: list = []
        self.minimum_admissions_per_year: float = 100
        self.minimum_thrombolysis_per_year: float = 3.3
        self.refit_ml_models: bool = True
        self.year_end: int = 2019
        self.year_start: int = 2017

        # Update the GlobVars object from imput arguments
        self.__dict__.update(args)
        self.__dict__.update(kwargs)

        # Load data
        self.load_data()

        # Restrict data
        self.restrict_data()

    def load_data(self):
        """
        Load data into the global variables object.
        """

        self.original_data: pd.DataFrame = pd.read_csv('./data/data.csv')

        required_fields: list = [
            'stroke team', 'age', 'male', 'infarction',
            'onset-to-arrival time', 'onset known', 'precise onset known',
            'onset during sleep', 'arrive by ambulance', 'year',
            'use of AF anticoagulants', 'prior disability',
            'arrival-to-scan time', 'thrombolysis',
            'scan-to-thrombolysis time', 'death', 'discharge disability'
        ]

        self.xgb_thrombolysis_fields: list = [
            'stroke team', 'age', 'male', 'infarction', 
            'onset-to-arrival time', 'onset known', 'precise onset known',
            'onset during sleep', 'use of AF anticoagulants',
            'prior disability', 'arrival-to-scan time', 'thrombolysis'
        ]

        # Check required fields are present
        for field in required_fields:
            assert field in self.original_data.columns, \
                f'Field {field} not present in data.'

    def restrict_data(self):
        """
        Restrict the data to prescribed limits of years, admissions and
        thrombolysis.
        """

        # Limit data to years of interest
        restricted_years_data: pd.DataFrame = self.original_data[
            (self.original_data['year'] >= self.year_start)
            & (self.original_data['year'] <= self.year_end)]

        # Calculate number of years
        number_of_years: int = self.year_end - self.year_start + 1

        # Create groupy object, by stroke team
        groupby = restricted_years_data.groupby('stroke team')

        # Loop through groupby object and check stroke team within limits
        for stroke_team, group in groupby:

            # Include the group by default
            include = True

            # Check number of admissions
            if len(group) / number_of_years < self.minimum_admissions_per_year:
                include = False

            # Check number of thrombolysis
            elif (group['thrombolysis'].sum() / number_of_years
                  < self.minimum_thrombolysis_per_year):
                include = False

            # If the group is to be included, append it to included teams list
            if include:
                self.included_teams.append(stroke_team)

        # Filter the original data to include only the included teams
        self.restricted_data = \
            self.original_data[self.original_data['stroke team'].isin(
                self.included_teams)]

        # Get list of excluded teams
        self.excluded_teams = \
            list(set(self.original_data['stroke team'].unique()) - set(
                self.included_teams))
        self.excluded_teams.sort()
