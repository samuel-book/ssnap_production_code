"""
Samual module.

This is the main co-ordinating module.

It contains the Samuel class.

"""

from globvars.globvars import GlobVars
from output.output import Output
from output.report import Report
from xgbmodel.xbg_thrombolysis_model import XGBThrombolysisModel


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

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the Samuel analysis model.

        Parameters:
        -----------
        globvars : object
            Object to store global variables.

        output : object
            Object to store the output of the simulation.

        report : object
            Object to store the report of the simulation.
        """

        # Set up global variables
        self.globvars: GlobVars = GlobVars(*args, **kwargs)

        # Set up output and report objects
        self.output: Output = Output(self.globvars)
        self.report: Report = Report(self.output)

        # Set up the XGB model
        self.XGBThrombolysisModel: XGBThrombolysisModel = \
            XGBThrombolysisModel(self.globvars)

    def run(self) -> None:
        """
        Run the Samuel simulation.
        """

        self.XGBThrombolysisModel.validate_model()
        #self.report.generate_report()
        #self.report.save('./output/report/report')
        
