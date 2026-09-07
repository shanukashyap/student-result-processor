from student_result import (
    create_student,
    calculate_result
)

from student_result.exceptions import (
    InvalidMarksError,
    MissingStudentInfoError
)

from student_result.logger import setup_logger


logger = setup_logger()


def process_student(name, marks):
    """Process one student's result."""

    try:
        student = create_student(name, marks)

        result = calculate_result(student["marks"])

        logger.info(
            f"Successfully processed student: {student['name']}"
        )

        print("\n" + "=" * 45)
        print(f"Student Name : {student['name']}")
        print(f"Marks        : {student['marks']}")
        print(f"Total        : {result['total']}")
        print(f"Percentage   : {result['percentage']:.2f}%")
        print(f"Grade        : {result['grade']}")
        print(f"Status       : {result['status']}")
        print("=" * 45)

    except InvalidMarksError as error:

        logger.error(
            f"Invalid marks for {name or 'Unknown'}: {error}"
        )

        print(
            f"\nError processing {name or 'Unknown'}: {error}"
        )

    except MissingStudentInfoError as error:

        logger.error(
            f"Missing student information: {error}"
        )

        print(
            f"\nError: {error}"
        )

    except (TypeError, ValueError, ZeroDivisionError) as error:

        logger.error(
            f"Calculation/input error for "
            f"{name or 'Unknown'}: {error}"
        )

        print(
            f"\nError processing {name or 'Unknown'}: {error}"
        )

    except Exception as error:

        logger.exception(
            f"Unexpected error for {name or 'Unknown'}: {error}"
        )

        print(
            f"\nUnexpected error: {error}"
        )


def main():

    print("=" * 55)
    print("       FAULT-TOLERANT STUDENT RESULT PROCESSOR")
    print("=" * 55)

    try:
        number_of_students = int(
            input("\nEnter number of students: ")
        )

        if number_of_students <= 0:
            raise ValueError(
                "Number of students must be greater than zero."
            )

    except ValueError as error:

        logger.error(
            f"Invalid number of students: {error}"
        )

        print(f"Error: {error}")
        return

    for student_number in range(1, number_of_students + 1):

        print(f"\n--- Student {student_number} ---")

        name = input("Enter student name: ").strip()

        marks = []

        for subject in range(1, 6):

            mark_input = input(
                f"Enter marks for Subject {subject}: "
            ).strip()

            try:
                mark = float(mark_input)
                marks.append(mark)

            except ValueError:

                logger.error(
                    f"Non-numeric mark for student "
                    f"{name or 'Unknown'}, "
                    f"Subject {subject}: {mark_input}"
                )

                print(
                    f"Invalid input: '{mark_input}' "
                    "is not a number."
                )

                # Mark the student as invalid.
                marks = []
                break

        if len(marks) != 5:

            print(
                "Student could not be processed. "
                "Moving to the next student."
            )

            continue

        process_student(name, marks)

    print("\nAll students have been processed.")
    print("Check student_result.log for details.")


if __name__ == "__main__":
    main()