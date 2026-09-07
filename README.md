# Fault-Tolerant Student Result Processor

## 📌 Project Overview

The **Fault-Tolerant Student Result Processor** is a Python project that reads student details and marks for 5 subjects and calculates:

- Total marks
- Percentage
- Grade
- Pass/Fail status

The program is designed to be **fault-tolerant**, meaning that when an error occurs for one student, the program logs the error and continues processing the remaining students instead of stopping completely.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate:

- Python functions
- Python modules
- Python packages
- Custom exceptions
- Exception handling
- Logging
- Input validation
- Fault-tolerant programming
- Separation of responsibilities between modules

---

## ✨ Features

### 1. Student Information

The program accepts:

- Student name
- Marks for 5 subjects

### 2. Result Calculation

For each valid student, the program calculates:

- **Total Marks**
- **Percentage**
- **Grade**
- **Pass/Fail Status**

### 3. Grade Calculation

| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| 40–49 | E |
| Below 40 | F |

### 4. Pass/Fail Rule

A student passes only when they score **40 or above in every subject**.

If the student scores below 40 in any subject, the result is:

```text
FAIL


🛡️ Error Handling

The program handles different types of errors without stopping the entire program.

The following errors are handled:

Missing student name
Non-numeric marks
Marks below 0
Marks above 100
Incorrect number of marks
Invalid number of students
Division/calculation errors
Unexpected errors

Errors are displayed to the user and recorded in the log file.

⚠️ Custom Exceptions

The project uses custom exceptions to make error handling clearer.

InvalidMarksError

Used when marks are outside the valid range of 0–100 or when the required number of marks is incorrect.

MissingStudentInfoError

Used when the student name is missing.

📁 Project Structure
student-result-processor/
│
├── student_result/
│   ├── __init__.py
│   ├── student.py
│   ├── result.py
│   ├── exceptions.py
│   └── logger.py
│
├── main.py
├── README.md
└── student_result.log
📂 Module Description
student.py

Responsible for:

Validating student information
Validating marks
Creating student records
result.py

Responsible for:

Calculating total marks
Calculating percentage
Calculating grade
Calculating pass/fail status
exceptions.py

Contains custom exceptions:

InvalidMarksError
MissingStudentInfoError
logger.py

Configures Python logging and stores errors and successful operations in:

student_result.log
__init__.py

Makes the student_result directory a Python package and exposes important functions and exceptions.

main.py

Acts as the main application.

It:

Accepts user input
Processes students
Handles errors
Displays results
Continues processing the next student
Logs errors and successful operations
▶️ How to Run
Step 1: Open the project in VS Code

Open the project folder:

student-result-processor
Step 2: Open the terminal

In VS Code, select:

Terminal → New Terminal
Step 3: Run the program
python main.py
Step 4: Enter the number of students

For example:

Enter number of students: 3

The program will then ask for the name and marks of each student.

🧪 Example
Input
Enter number of students: 2

--- Student 1 ---
Enter student name: Rahul
Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Enter marks for Subject 3: 78
Enter marks for Subject 4: 88
Enter marks for Subject 5: 92

--- Student 2 ---
Enter student name: Priya
Enter marks for Subject 1: 95
Enter marks for Subject 2: abc

The invalid mark is logged and the program continues with the next student.

📊 Sample Output
=============================================
Student Name : Rahul
Marks        : [85.0, 90.0, 78.0, 88.0, 92.0]
Total        : 433.0
Percentage   : 86.60%
Grade        : A
Status       : PASS
=============================================

Invalid input: 'abc' is not a number.

Student could not be processed.
Moving to the next student.

All students have been processed.
Check student_result.log for details.
📝 Logging

The program creates a log file:

student_result.log

The log records:

Successful student processing
Invalid marks
Missing student information
Non-numeric input
Invalid student count
Calculation errors
Unexpected errors

Example:

2026-09-07 08:20:10 - INFO - Successfully processed student: Rahul
2026-09-07 08:20:15 - ERROR - Non-numeric mark for student Priya, Subject 2: abc
🧠 Fault Tolerance

One of the main features of this project is fault tolerance.

For example, if there are 3 students:

Student 1 → Valid
Student 2 → Invalid marks
Student 3 → Valid

The program does not stop after Student 2.

Instead:

Student 1 → Processed ✅
Student 2 → Error logged ❌
Student 3 → Processed ✅

This ensures that one incorrect input does not terminate the entire program.

🐍 Python Concepts Demonstrated

This project demonstrates the following Python concepts:

Functions
Modules
Packages
Imports
Dictionaries
Lists
Loops
Conditional statements
try-except
Custom exceptions
Logging
Input validation
File/module organization
📚 What I Learned

Through this project, I learned how to:

Create a modular Python application
Divide functionality into separate modules
Create and use custom exceptions
Validate user input
Handle errors using try-except
Use Python's logging module
Continue program execution after errors
Create a reusable Python package
Separate business logic from the main application
👤 Author

Urmil Kashyap

🔗 Submission Links
GitHub

[Add your GitHub repository link here]

YouTube

[Add your YouTube video link here]


### One important point

Since this is a **Super30 assignment**, I recommend keeping the README focused on the assignment requirements rather than making it extremely long.

The most important sections are:

1. **Project Overview**
2. **Objective**
3. **Features**
4. **Error Handling**
5. **Custom Exceptions**
6. **Project Structure**
7. **Module Description**
8. **How to Run**
9. **Sample Output**
10. **Logging**
11. **Fault Tolerance**
12. **Python Concepts**
13. **Author**

