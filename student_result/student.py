from .exceptions import InvalidMarksError, MissingStudentInfoError


NUMBER_OF_SUBJECTS = 5


def validate_student_name(name):
    """Validate student name."""

    if not name or not name.strip():
        raise MissingStudentInfoError(
            "Student name cannot be empty."
        )

    return name.strip()


def validate_marks(marks):
    """Validate marks for all five subjects."""

    if len(marks) != NUMBER_OF_SUBJECTS:
        raise InvalidMarksError(
            "Exactly 5 subject marks are required."
        )

    for mark in marks:

        if isinstance(mark, bool):
            raise TypeError("Marks must be numeric.")

        if not isinstance(mark, (int, float)):
            raise TypeError(
                "Marks must be numeric."
            )

        if mark < 0 or mark > 100:
            raise InvalidMarksError(
                f"Invalid mark: {mark}. "
                "Marks must be between 0 and 100."
            )

    return marks


def create_student(name, marks):
    """Create and validate student data."""

    name = validate_student_name(name)
    marks = validate_marks(marks)

    return {
        "name": name,
        "marks": marks
    }