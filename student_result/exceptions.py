class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range."""

    pass


class MissingStudentInfoError(Exception):
    """Raised when student information is missing."""

    pass