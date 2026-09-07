def calculate_total(marks):
    """Calculate total marks."""

    if not marks:
        raise ValueError("Marks cannot be empty.")

    return sum(marks)


def calculate_percentage(marks):
    """Calculate percentage."""

    if not marks:
        raise ValueError("Marks cannot be empty.")

    total = calculate_total(marks)

    return total / (len(marks) * 100) * 100


def calculate_grade(percentage):
    """Calculate grade based on percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage >= 40:
        return "E"

    else:
        return "F"


def calculate_pass_fail(marks):
    """Determine pass or fail status."""

    # Student must score at least 40 in every subject.
    if all(mark >= 40 for mark in marks):
        return "PASS"

    return "FAIL"


def calculate_result(marks):
    """Calculate complete student result."""

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    status = calculate_pass_fail(marks)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }