class Output(object):

    """
    This class holds the model output. It is a container for the output.
    This class will be used to build a report.

    ...

    Attributes:
    -----------

    globvars : object
        Object to store global variables.

    Methods:
    --------

    """

    def __init__(self, globvars: object) -> None:
        """
        Constructor for the Output class.
        """

        # Store global variables
        self.globvars = globvars
