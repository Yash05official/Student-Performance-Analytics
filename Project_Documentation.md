# Student Performance Analytics System

## 1. Project Title and Student Details

**Project Title:** Student Performance Analytics System  
**Student Name:** Yash Rahul Kamble  
**Course:** EWB Courses – Python with AI  
**Branch/Department:** ENTC  
**Project Type:** Python Data Analytics Project

## 2. Objective

The objective of this project is to analyze student academic performance using Python. The system processes student marks and attendance to calculate total marks, average marks, grades, and pass/fail results.

It also summarizes class performance, compares subject averages, identifies top and low-performing students, and provides an interactive dashboard to explore the results. The project demonstrates how data analysis can help organize academic information and identify areas for improvement.

## 3. Technologies Used

- **Python:** Implements the project logic and reusable functions.
- **NumPy:** Supports numerical operations.
- **Pandas:** Loads, processes, filters, analyzes, and exports tabular data.
- **Streamlit:** Creates the interactive web dashboard.
- **Plotly:** Creates interactive charts and visualizations.
- **Pytest:** Tests the calculation and analysis functions.
- **Git and GitHub:** Manage and publish the project source code.

## 4. Dataset Description

The project uses a CSV dataset named `students.csv` containing approximately 20 sample student records.

The dataset contains the following columns:

- `Student_ID`: Unique student identifier.
- `Name`: Student name.
- `Department`: Student's department.
- `Python`: Marks obtained in Python.
- `Mathematics`: Marks obtained in Mathematics.
- `AI`: Marks obtained in Artificial Intelligence.
- `Attendance`: Student attendance percentage.

The dataset is used for demonstrating academic analysis. The sample records are not intended to represent official student results.

## 5. Implementation

### Step 1: Data Loading

The Pandas library reads the CSV dataset into a DataFrame. The program checks that the required columns are present before analysis.

### Step 2: Data Validation

The validation function checks for missing values, duplicate student IDs, non-numeric marks, and marks or attendance values outside the expected range of 0–100.

### Step 3: Student Performance Calculation

Reusable functions calculate each student's total marks and average marks across Python, Mathematics, and AI. Grades are assigned based on the calculated average.

### Step 4: Pass/Fail Evaluation

The program marks a student as Pass only when all three subject marks are at least 40. Students with incomplete subject marks are classified as Incomplete.

### Step 5: Statistical Analysis

Pandas operations calculate class statistics, subject-wise averages, department performance, result distribution, and attendance information. The program also identifies the highest- and lowest-performing students.

NumPy is included for numerical operations and supports the project's numerical calculations.

### Step 6: Dashboard Development

Streamlit displays summary metrics, charts, filters, and student records. Plotly is used to visualize subject averages, grade distribution, department performance, and the relationship between attendance and average marks.

### Step 7: Report Generation

The main program exports the analyzed student records to `student_performance_report.csv`. The dashboard also provides a downloadable report for the selected records.

### Step 8: Testing

Pytest is used to test grade boundaries, pass/fail conditions, calculated student results, and class statistics.

## 6. Key Features

1. CSV dataset loading and validation.
2. Total and average marks calculation.
3. Automatic grade assignment.
4. Pass, Fail, and Incomplete result classification.
5. Class summary statistics.
6. Subject-wise average analysis.
7. Identification of top performers and students needing improvement.
8. Department-wise performance analysis.
9. Attendance analysis and identification of attendance below 75%.
10. Interactive dashboard with charts and filters.
11. Student record search and CSV report export.
12. Automated tests for core functions.

## 7. Output and Screenshots

Add screenshots of the actual project output in this section.

Suggested screenshots:

- Main program output in the VS Code terminal.
- Interactive Streamlit dashboard.
- Subject-wise average chart.
- Grade distribution chart.
- Department performance chart.
- Student records table and report download option.
- Successful test results from Pytest.

Each screenshot should have a short caption explaining what it demonstrates.

## 8. Final Outcome

The project provides a structured way to analyze student performance from a CSV dataset. It calculates academic metrics, assigns grades, classifies results, summarizes attendance, and displays visual reports through an interactive dashboard.

The project demonstrates the practical use of Python, NumPy, Pandas, Streamlit, and Plotly in a small data analytics application.

## 9. Challenges and Learning

The project involved organizing code into reusable functions, validating input data, calculating results consistently, setting up the required Python libraries, and connecting the analysis to an interactive dashboard.

These tasks helped develop practical skills in Python programming, DataFrame operations, data visualization, testing, debugging, and GitHub version control.

Update this section with the actual errors you encountered and how you resolved them.

## 10. GitHub Repository

**Repository URL:** [Paste your actual GitHub repository URL here]

The repository contains the project source code, dataset, setup instructions, tests, and project documentation.

## Conclusion

The Student Performance Analytics System demonstrates how Python-based data processing and visualization can convert student records into useful academic summaries. It provides a foundation for further improvements, such as additional analytics, improved validation, and more dashboard features.