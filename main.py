
"""Student Performance Analytics - Main Analysis"""

from pathlib import Path

import pandas as pd

from functions import (
    SUBJECTS,
    REQUIRED_COLUMNS,
    validate_data,
    analyze_data,
    summary_statistics,
    subject_averages,
    top_performers,
    lowest_performers,
    result_counts,
    department_performance,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"


def load_data(file_path=DATA_FILE):
    """Load the CSV file and check required columns."""

    df = pd.read_csv(file_path)

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    return df


def main():
    """Run the complete Student Performance Analytics program."""

    # Load student records
    df = load_data()

    # Validate the input data
    issues = validate_data(df)

    # Calculate totals, averages, grades and results
    analyzed = analyze_data(df)

    print("\n===== STUDENT PERFORMANCE ANALYTICS =====")

    # Display data validation messages
    if issues:
        print("\nDATA QUALITY WARNINGS:")

        for issue in issues:
            print("-", issue)
    else:
        print("\nData validation passed.")

    # Display the student report
    columns = [
        "Student_ID",
        "Name",
        "Department",
        "Total",
        "Average",
        "Grade",
        "Result",
        "Attendance",
    ]

    print("\n===== STUDENT REPORT =====")
    print(analyzed[columns].to_string(index=False))

    # Display class statistics
    print("\n===== CLASS STATISTICS =====")

    statistics = summary_statistics(analyzed)

    for key, value in statistics.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    # Display subject-wise averages
    print("\n===== SUBJECT-WISE AVERAGES =====")

    print(
        subject_averages(analyzed).to_string(index=False)
    )

    # Display top five students
    print("\n===== TOP 5 STUDENTS =====")

    top_students = top_performers(analyzed, 5)

    if top_students.empty:
        print("No student records available.")
    else:
        print(
            top_students[
                ["Student_ID", "Name", "Average", "Grade"]
            ].to_string(index=False)
        )

    # Display five students with the lowest averages
    print("\n===== STUDENTS NEEDING IMPROVEMENT =====")

    lowest_students = lowest_performers(analyzed, 5)

    if lowest_students.empty:
        print("No student records available.")
    else:
        print(
            lowest_students[
                ["Student_ID", "Name", "Average", "Grade"]
            ].to_string(index=False)
        )

    # Display pass, fail and incomplete counts
    print("\n===== RESULT DISTRIBUTION =====")

    counts = result_counts(analyzed)

    for result, count in counts.items():
        print(f"{result}: {count}")

    # Display department performance
    print("\n===== DEPARTMENT PERFORMANCE =====")

    department_report = department_performance(analyzed)

    if department_report.empty:
        print("No department data available.")
    else:
        print(department_report.to_string(index=False))

    # Display attendance analysis
    print("\n===== ATTENDANCE ANALYSIS =====")

    attendance_average = analyzed["Attendance"].mean()

    if pd.isna(attendance_average):
        print("Average attendance: Not available")
    else:
        print(
            f"Average attendance: {attendance_average:.2f}%"
        )

    # Find students with attendance below 75%
    low_attendance = analyzed[
        analyzed["Attendance"] < 75
    ]

    print("\n===== STUDENTS WITH ATTENDANCE BELOW 75% =====")

    if low_attendance.empty:
        print("No students found.")
    else:
        print(
            low_attendance[
                ["Student_ID", "Name", "Attendance"]
            ].to_string(index=False)
        )

    # Save the complete report to a new CSV file
    output_file = BASE_DIR / "student_performance_report.csv"

    analyzed.to_csv(output_file, index=False)

    print("\n===== REPORT SAVED SUCCESSFULLY =====")
    print(f"File location: {output_file}")


if __name__ == "__main__":
    main()
