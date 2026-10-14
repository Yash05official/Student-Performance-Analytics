
"""Reusable functions for Student Performance Analytics."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "AI"]

REQUIRED_COLUMNS = [
    "Student_ID",
    "Name",
    "Department",
    "Python",
    "Mathematics",
    "AI",
    "Attendance",
]


def validate_data(df):
    """Check for missing data, duplicate IDs and invalid values."""
    issues = []

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        return [
            f"Missing required columns: {', '.join(missing_columns)}"
        ]

    for column in REQUIRED_COLUMNS:
        missing_count = int(df[column].isna().sum())

        if missing_count > 0:
            issues.append(
                f"{column}: {missing_count} missing value(s)"
            )

    if df["Student_ID"].duplicated().any():
        issues.append("Student_ID contains duplicate values.")

    for subject in SUBJECTS:
        values = pd.to_numeric(df[subject], errors="coerce")

        invalid = values.notna() & ~values.between(0, 100)
        non_numeric = df[subject].notna() & values.isna()

        if invalid.any():
            issues.append(
                f"{subject} contains marks outside 0–100."
            )

        if non_numeric.any():
            issues.append(
                f"{subject} contains non-numeric marks."
            )

    attendance = pd.to_numeric(
        df["Attendance"], errors="coerce"
    )

    invalid_attendance = (
        attendance.notna()
        & ~attendance.between(0, 100)
    )

    if invalid_attendance.any():
        issues.append(
            "Attendance contains values outside 0–100."
        )

    non_numeric_attendance = (
        df["Attendance"].notna() & attendance.isna()
    )

    if non_numeric_attendance.any():
        issues.append("Attendance contains non-numeric values.")

    return issues


def calculate_total(row):
    """Calculate total marks across all subjects."""
    marks = pd.to_numeric(
        row[SUBJECTS], errors="coerce"
    )

    if marks.isna().any():
        return np.nan

    return float(marks.sum())


def calculate_average(row):
    """Calculate average marks across all subjects."""
    marks = pd.to_numeric(
        row[SUBJECTS], errors="coerce"
    )

    if marks.isna().any():
        return np.nan

    return round(float(marks.mean()), 2)


def calculate_grade(average):
    """Assign a grade based on average marks."""
    if pd.isna(average):
        return "N/A"
    elif average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def calculate_result(row):
    """Pass when every subject mark is at least 40."""
    marks = pd.to_numeric(
        row[SUBJECTS], errors="coerce"
    )

    if marks.isna().any():
        return "Incomplete"

    if (marks >= 40).all():
        return "Pass"

    return "Fail"


def analyze_data(df):
    """Calculate total, average, grade and result for each student."""
    result = df.copy()

    for column in SUBJECTS + ["Attendance"]:
        result[column] = pd.to_numeric(
            result[column], errors="coerce"
        )

    result["Total"] = result.apply(calculate_total, axis=1)

    result["Average"] = result.apply(
        calculate_average, axis=1
    )

    result["Grade"] = result["Average"].apply(calculate_grade)

    result["Result"] = result.apply(
        calculate_result, axis=1
    )

    return result


def summary_statistics(df):
    """Calculate overall class performance statistics."""
    averages = df["Average"].dropna()
    total_students = len(df)

    passed = int((df["Result"] == "Pass").sum())
    failed = int((df["Result"] == "Fail").sum())
    incomplete = int((df["Result"] == "Incomplete").sum())

    return {
        "total_students": total_students,
        "class_average": (
            round(float(averages.mean()), 2)
            if not averages.empty else 0
        ),
        "highest_average": (
            round(float(averages.max()), 2)
            if not averages.empty else 0
        ),
        "lowest_average": (
            round(float(averages.min()), 2)
            if not averages.empty else 0
        ),
        "passed": passed,
        "failed": failed,
        "incomplete": incomplete,
        "pass_percentage": (
            round(passed / total_students * 100, 2)
            if total_students else 0
        ),
        "average_attendance": (
            round(float(df["Attendance"].mean()), 2)
            if df["Attendance"].notna().any() else 0
        ),
    }


def subject_averages(df):
    """Calculate the average marks for each subject."""
    return (
        df[SUBJECTS]
        .mean()
        .round(2)
        .rename_axis("Subject")
        .reset_index(name="Average Marks")
    )


def top_performers(df, count=5):
    """Return the students with the highest averages."""
    return df.nlargest(count, "Average")


def lowest_performers(df, count=5):
    """Return the students with the lowest averages."""
    return df.nsmallest(count, "Average")


def result_counts(df):
    """Count students in each result category."""
    return df["Result"].value_counts()


def department_performance(df):
    """Calculate student count and average by department."""
    return (
        df.groupby("Department")
        .agg(
            Total_Students=("Student_ID", "count"),
            Average_Marks=("Average", "mean"),
        )
        .round(2)
        .reset_index()
    )
