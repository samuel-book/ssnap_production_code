import output.output
from globvars import GlobVars

class Samuel(object):
    """
    Main class for the Samuel simulation.
    
    ...

    Parameters:
    -----------
    globvars : object
        Object to store global variables.


    Methods:
    --------

    __init__(self, *args, **kwargs):
        Initialize the Samuel analysis model.

    run():
        Run the Samuel simulation.

    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the Samuel analysis model.

        Parameters:
        -----------
        globvars : object
            Object to store global variables.
        """
        
        # Set up global variables
        self.globvars:object = GlobVars(*args, **kwargs)
    
    def run(self):
        """
        Run the Samuel simulation.
        """
        
        pass


if __name__ == "__main__":
    """
    Main function.
    """

    sam = Samuel()
    sam.run()