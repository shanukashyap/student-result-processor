import logging


def setup_logger():
    """Configure application logging."""

    logging.basicConfig(
        filename="student_result.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("student_result")