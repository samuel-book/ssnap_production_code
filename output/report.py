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

    generate_chapter_units_in_scope:
        Generate chapter which lists units in scope:

    generate_report(self):
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

        # Create a new empty pylatex document
        self.doc: pylatex.Document = pylatex.Document()

    def add_packages(self) -> None:
        """
        Add packages to the report.
        """

        self.doc.packages.append(pylatex.Package('geometry', options=[
            'a4paper', 'margin=2cm']))
        self.doc.packages.append(pylatex.Package('microtype'))
        self.doc.append(pylatex.NoEscape(r'\linespread{1.2}'))

    def generate_title_pages(self) -> None:
        """
        Generate the title page, and table of contents.
        Includes adding required LaTeX packages.
        """
        # Add packages
        self.add_packages()

        # Build title
        self.doc.preamble.append(pylatex.Command('title', 'SAMueL Report'))
        self.doc.preamble.append(pylatex.Command('author', 'Samuel'))
        self.doc.preamble.append(pylatex.Command(
            'date', pylatex.NoEscape(r'\today')))
        self.doc.append(pylatex.NoEscape(r'\maketitle'))

        self.doc.append(pylatex.NoEscape(r'\tableofcontents'))

        self.doc.append(pylatex.NoEscape(r'\newpage'))

    def generate_chapter_units_in_scope(self) -> None:
        """List units in scope, and those excluded."""

        self.doc.append(pylatex.Section('Units in scope'))

        # Preamble

        txt = (
            'For units to be in scope thay must have an average number ' +
            'of yearly admissions of at least ' +
            f'{self.output.globvars.minimum_admissions_per_year}, and an ' +
            'average number of yearly thrombolysed patients of at least ' +
            f'{self.output.globvars.minimum_thrombolysis_per_year}.\n\n')
        self.doc.append(txt)

        txt = (
            f'Start year (inclusive): {self.output.globvars.year_start}\n' +
            f'End year (inclusive): {self.output.globvars.year_end}\n\n')
        self.doc.append(txt)

        # Count number of units included
        self.doc.append(
            'Number of units in scope: ' +
            f'{len(self.output.globvars.included_teams)}\n\n')

        self.doc.append('Units included:')

        # Change text size to small
        self.doc.append(pylatex.Command('footnotesize'))

        # List included units
        with self.doc.create(pylatex.Itemize()) as itemize:
            # Add each item from the Python list to the itemized list
            for unit in self.output.globvars.included_teams:
                itemize.add_item(unit)
        self.doc.append(pylatex.Command('normalsize'))

    def generate_report(self) -> None:
        """
        Generate the report.
        This method calls separate methods to compile the report
        """

        self.generate_title_pages()
        self.generate_chapter_units_in_scope()

    def save(self, filename: str) -> None:
        """
        Save the report to a file: Creates .tex, .toc, and .pdf files.
        """

        self.doc.generate_pdf(filename, clean_tex=False)
