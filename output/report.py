"""
This module contains the Report class.
This class builds and saves the report.
"""


import pylatex

from output.output import Output


class Report(object):
    """
    This class builds the report.

    ...

    Attributes:
    -----------

    output: object
        The output from the SAMuel model.

    doc: object
        The pylatex document.


    Methods:
    --------

    gererate_report(self):
        Generate the report.

    generate_title_pages(self):
        Generate the title pages.

    save(self, filename):
        Save the report to a file.
    """

    def __init__(self, output: Output) -> None:
        """
        Constructor for the Report class.
        """

        # Store the output from the SAMuel model
        self.output: Output = output

        # Create a new pylatex document
        self.doc: pylatex.Document = pylatex.Document()

    def generate_title_pages(self) -> None:
        """
        Generate the title pages.
        """

        self.doc.preamble.append(pylatex.Command('title', 'Samuel Report'))
        self.doc.preamble.append(pylatex.Command('author', 'Samuel'))
        self.doc.preamble.append(pylatex.Command(
            'date', pylatex.NoEscape(r'\today')))
        self.doc.append(pylatex.NoEscape(r'\maketitle'))

        self.doc.append(pylatex.NoEscape(r'\tableofcontents'))

        self.doc.append(pylatex.NoEscape(r'\newpage'))

    def generate_report(self) -> None:
        """
        Generate the report.
        """

        self.generate_title_pages()

        # Placeholder to show how to add section title
        # self.doc.append(pylatex.Section('Introduction'))

    def save(self, filename: str) -> None:
        """
        Save the report to a file.
        """

        self.doc.generate_pdf(filename, clean_tex=False)
