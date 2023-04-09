from globvars import GlobVars
from output.output import Output
from output.report import Report


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
        self.globvars: object = GlobVars(*args, **kwargs)

    def run(self):
        """
        Run the Samuel simulation.
        """

        self.output = Output()
        self.report = Report(self.output)
        self.report.generate_report()
        self.report.save('./output/report/report')


if __name__ == "__main__":
    """
    Main function.
    """

    sam = Samuel(minimum_admissions_per_year=600)
    sam.run()
