from samuel.samuel import Samuel


if __name__ == "__main__":
    """
    Main function.
    """

    sam: Samuel = Samuel(minimum_admissions_per_year=100)
    sam.run()
