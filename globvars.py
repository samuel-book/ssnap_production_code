class GlobVars:
    """
    Object to store global variables
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the global variables object.
        """

        self.test = 10 

        # Update the GlobVars object with keyword arguments passed to the constructor
        self.__dict__.update(kwargs)

