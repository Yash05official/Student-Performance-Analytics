
# Student Performance Analytics System

A Python-based data analysis project that evaluates student marks,
grades, pass/fail status, attendance and academic performance.

## Features

- Load student records from CSV using Pandas.
- Calculate total and average marks.
- Assign grades using defined grading rules.
- Identify pass/fail students.
- Calculate class and subject-wise averages.
- Identify top-performing students.
- Analyze attendance.
- Detect common data-quality issues.
- Display interactive charts and summary cards.
- Filter by department and result.
- Search student records.
- Download filtered reports as CSV.
- Run automated tests using pytest.

## Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- pytest

## Project Structure

- `main.py` - Analysis functions and terminal report.
- `dashboard.py` - Interactive web dashboard.
- `students.csv` - Sample dataset.
- `tests/test_analysis.py` - Automated tests.
- `requirements.txt` - Python dependencies.
- `Project_Documentation.md` - Project report.

## Installation

Create a virtual environment:

```powershell
py -m venv .venv
```

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the Terminal Report

```powershell
.\.venv\Scripts\python.exe main.py
```

## Run the Dashboard

```powershell
.\.venv\Scripts\python.exe -m streamlit run dashboard.py
```

Open the local URL displayed in the terminal.

## Run Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Grading Rules

- A+: average of 90 or above.
- A: average of 80 to below 90.
- B: average of 70 to below 80.
- C: average of 60 to below 70.
- D: average of 40 to below 60.
- F: average below 40.

A student passes only if each subject mark is at least 40.
Attendance is analyzed separately.

These are example rules for this project, not official college rules.

## Dataset

The included dataset contains 20 fictional student records.
Do not publish real student information without authorization.

## Limitations

This is a learning project using a small sample dataset.
It does not predict future academic performance or verify
official academic records.

## Future Improvements

- Database integration.
- User login and role-based access.
- Larger authorized datasets.
- More detailed reporting and analytics.

## GitHub Repository

Add your actual GitHub repository URL here.
