
import pandas as pd

from functions import (
    analyze_data,
    calculate_grade,
    calculate_result,
    summary_statistics,
)


def test_grade_boundaries():
    """Check that grades are assigned correctly at each boundary."""
    assert calculate_grade(90) == "A+"
    assert calculate_grade(80) == "A"
    assert calculate_grade(70) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(40) == "D"
    assert calculate_grade(39.99) == "F"


def test_pass_requires_every_subject_to_be_40():
    """A student passes only when every subject mark is at least 40."""
    passing = pd.Series({
        "Python": 40,
        "Mathematics": 50,
        "AI": 60,
    })

    failing = pd.Series({
        "Python": 42,
        "Mathematics": 39,
        "AI": 80,
    })

    assert calculate_result(passing) == "Pass"
    assert calculate_result(failing) == "Fail"


def test_analysis_adds_expected_columns():
    """Check total, average, grade and result calculations."""
    df = pd.DataFrame([{
        "Student_ID": 1,
        "Name": "Test",
        "Department": "ENTC",
        "Python": 90,
        "Mathematics": 80,
        "AI": 100,
        "Attendance": 95,
    }])

    analyzed = analyze_data(df)

    assert analyzed.loc[0, "Total"] == 270
    assert analyzed.loc[0, "Average"] == 90
    assert analyzed.loc[0, "Grade"] == "A+"
    assert analyzed.loc[0, "Result"] == "Pass"


def test_summary_statistics():
    """Check that class statistics are calculated correctly."""
    df = pd.DataFrame([{
        "Student_ID": 1,
        "Name": "Test",
        "Department": "IT",
        "Python": 80,
        "Mathematics": 80,
        "AI": 80,
        "Attendance": 90,
    }])

    analyzed = analyze_data(df)
    stats = summary_statistics(analyzed)

    assert stats["total_students"] == 1
    assert stats["passed"] == 1
    assert stats["failed"] == 0
    assert stats["pass_percentage"] == 100
