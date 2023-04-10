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
            The list of stroke teams excluded from the analysis, as obtained by applying
            prescribed limits to the data.
        
        included_teams: list
            The list of stroke teams included in the analysis, as obtained by applying
            prescribed limits to the data.
        
        minimum_admissions_per_year: float
            The minimum number of admissions per year to be included in the analysis.
        
        minimum_thrombolysis_per_year: float
            The minimum number of thrombolysis per year to be included in the analysis.
        
        year_end: int
            The last year of the data to be used in the analysis.
        
        year_start: int
            The first year of the data to be used in the analysis.
        """

        self.excluded_teams: list = []
        self.included_teams: list = []
        self.minimum_admissions_per_year: float = 100
        self.minimum_thrombolysis_per_year: float = 3.3
        self.year_end: int = 2019
        self.year_start: int = 2017
    

        # Update the GlobVars object with keyword arguments passed to the constructor
        self.__dict__.update(args)
        self.__dict__.update(kwargs)

        # Load data
        self.load_data()

        # Restrict data
        self.reset_data()
        

    def load_data(self):
        """
        Load data into the global variables object.
        """

        self.original_data: pd.DataFrame = pd.read_csv('./data/data.csv')

    def reset_data(self):
        """
        Restrict the data to prescribed limits
        """

        number_of_years: int = self.year_end - self.year_start + 1
        
        # Create groupy object, by stroke team
        groupby = self.original_data.groupby('stroke team')

        # Loop through groupby object and check stroke team within limits
        for stroke_team, group in groupby:

            # Include the group by default
            include = True

            # If the number of admissions is less than the minimum, drop the group
            if len(group) / number_of_years < self.minimum_admissions_per_year:
                include = False

            # If the number of thrombolysis is less than the minimum, drop the group
            elif group['thrombolysis'].sum() / number_of_years < self.minimum_thrombolysis_per_year:
                include = False

            # If the group is to be included, append it to included teams list
            if include:
                self.included_teams.append(stroke_team)

        # Filter the original data to include only the included teams
        self.restricted_data = \
            self.original_data[self.original_data['stroke team'].isin(self.included_teams)]
        
        # Get list of excluded teams
        self.excluded_teams = \
            list(set(self.original_data['stroke team'].unique()) - set(self.included_teams))
        self.excluded_teams.sort()






