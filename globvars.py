import pandas as pd

class GlobVars:
    """
    Object to store global variables
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the global variables object.
        """

        # Update the GlobVars object with keyword arguments passed to the constructor
        self.__dict__.update(args)
        self.__dict__.update(kwargs)

        # Load data
        self.load_data()


    def load_data(self):
        """
        Load data into the global variables object.
        """

        self.original_data: pd.DataFrame = pd.read_csv('./data/data.csv')



