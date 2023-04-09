import pylatex

class Report(object):
    """
    This class builds the report.
    """

    def __init__(self, output):
        """
        Constructor for the Report class.
        """

        # Store the output from the SAMuel model
        self.output: object = output

        # Create a new pylatex document
        self.doc: pylatex_document = pylatex.Document()


    def generate_title_pages(self):
        """
        Generate the title pages.
        """

        self.doc.preamble.append(pylatex.Command('title', 'Samuel Report'))
        self.doc.preamble.append(pylatex.Command('author', 'Samuel'))
        self.doc.preamble.append(pylatex.Command('date', pylatex.NoEscape(r'\today')))
        self.doc.append(pylatex.NoEscape(r'\maketitle'))

        self.doc.append(pylatex.NoEscape(r'\tableofcontents'))

        self.doc.append(pylatex.NoEscape(r'\newpage'))


    def generate_report(self):       
        """
        Generate the report.
        """

        self.generate_title_pages()

        # Placeholder to show how to add section title
        # self.doc.append(pylatex.Section('Introduction'))



    def save(self, filename):
        """
        Save the report to a file.
        """

        self.doc.generate_pdf(filename, clean_tex=False)